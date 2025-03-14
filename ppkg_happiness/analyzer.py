import os
import re
import sys
import json
import shutil
import magic
import hashlib
import argparse
import tempfile
import subprocess
from bs4 import BeautifulSoup

BIG_DUMB_CUP = [
    ".exe",
    ".dll",
    ".ocx",
    ".cpl",
    ".scr",
    ".msi",
    ".msp",
    ".bat",
    ".cmd",
    ".ps1",
    ".vbs",
    ".js",
    ".hta",
    ".wsf",
    ".py",
    ".pl",
    ".jar",
    ".doc",
    ".docx",
    ".rtf",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".pdf",
    ".zip",
    ".cab",
    ".rar",
    ".7z",
    ".img",
    ".iso",
    ".vhd",
    ".vhdx",
    ".vmdk",
    ".ova",
    ".ovf",
    ".tar",
    ".gz",
    ".bz2",
    ".xz",
    ".lzma",
    ".zst",
    ".lz4",
    ".lzh",
    ".arj",
    ".arc",
    ".zoo",
    ".pak",
    ".alz",
    ".ace",
    ".uha",
    ".r01",
    ".r02",
    ".r03",
    ".r04",
    ".r05",
    ".r06",
    ".r07",
    ".r08",
    ".r09",
    ".r10",
    ".r11",
    ".r12",
    ".r13",
    ".r14",
    ".r15",
    ".r16",
    ".r17",
    ".r18",
    ".r19",
    ".r20",
    ".r21",
    ".r22",
    ".r23",
    ".r24",
    ".r25",
    ".r26",
    ".r27",
    ".r28",
    ".r29",
    ".r30",
    ".r31",
    ".r32",
    ".r33",
    ".r34",
    ".r35",
    ".r36",
    ".r37",
    ".r38",
    ".r39",
    ".r40",
    ".r41",
    ".r42",
    ".r43",
    ".r44",
    ".r45",
    ".r46",
    ".r47",
    ".r48",
    ".r49",
    ".r50",
    ".r51",
    ".r52",
    ".r53",
    ".r54",
    ".r55",
    ".r56",
    ".r57",
    ".r58",
    ".r59",
    ".r60",
    ".r61",
    ".r62",
    ".r63",
    ".r64",
    ".r65",
    ".r66",
    ".r67",
    ".r68",
    ".r69",
    ".r70",
    ".r71",
    ".r72",
    ".r73",
    ".r74",
    ".r75",
    ".r76",
    ".r77",
    ".r78",
    ".r79",
    ".r80",
    ".r81",
    ".r82",
    ".r83",
    ".r84",
    ".r85",
    ".r86",
    ".r87",
    ".r88",
    ".r89",
    ".r90",
    ".r91",
    ".r92",
    ".r93",
    ".r94",
    ".r95",
    ".r96",
    ".r97",
    ".r98",
    ".r99",
    ".r100",
    ".r101",
    ".r102",
    ".r103",
    ".r104",
    ".r105",
    ".r106",
    ".html",
    ".htm",
    ".chm",
    ".mht",
    ".mhtml",
    ".vbe",
    ".jse",
    ".slk",
    ".csv",
    ".msc",
]


class PpkgPursuitOfHappiness:
    """
    - Returns a JSON-like dict. On errors, returns empty or partial structure + error info.
    """

    def __init__(self, input_file, output_dir, json_file=None):
        self.ppkg_path = input_file
        self.output_dir = output_dir
        self.json_file = json_file

        # Our final JSON-like data structure
        self.final_report = {"ppkgMetadata": {}, "commands": [], "fileDetails": [], "copiedDataAssets": []}  # from <PackageConfig>

    def _get_mime_type(self, file_path):
        try:
            return magic.from_file(file_path, mime=True)
        except:
            return "application/octet-stream"

    def _extract_with_7z(self, extract_dir):
        cmd = ["7z", "x", "-y", f"-o{extract_dir}", self.ppkg_path]
        with open(os.devnull, "wb") as devnull:
            subprocess.run(cmd, check=True, stdout=devnull, stderr=devnull)

    def _compute_hashes(self, file_path):
        chunk_size = 1024 * 1024
        md5_obj = hashlib.md5()
        sha1_obj = hashlib.sha1()
        sha256_obj = hashlib.sha256()
        with open(file_path, "rb") as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                md5_obj.update(data)
                sha1_obj.update(data)
                sha256_obj.update(data)
        return {"md5": md5_obj.hexdigest(), "sha1": sha1_obj.hexdigest(), "sha256": sha256_obj.hexdigest()}

    def _parse_for_commands(self, soup):
        commands = []
        provisioning_nodes = soup.find_all(re.compile(r"^ProvisioningCommands$", re.IGNORECASE))
        for prov_node in provisioning_nodes:
            cmd_nodes = prov_node.find_all(re.compile(r"^CommandLine$", re.IGNORECASE))
            for c in cmd_nodes:
                commands.append(c.get_text(strip=True))
        return commands

    def _parse_package_config(self, soup):
        pkg_config = soup.find("PackageConfig")
        if not pkg_config:
            return None

        def parse_node(node):
            result_data = {}
            for child in node.find_all(recursive=False):
                if not child.name:
                    continue

                child_name = child.name

                sub_children = [c for c in child.find_all(recursive=False) if c.name]

                if sub_children:
                    val = parse_node(child)
                else:
                    val = child.get_text(strip=True)

                if child_name in result_data:
                    existing = result_data[child_name]
                    if not isinstance(existing, list):
                        result_data[child_name] = [existing]
                    result_data[child_name].append(val)
                else:
                    result_data[child_name] = val

            return result_data

        result = parse_node(pkg_config)
        return result if result else None

    def _parse_dataasset_xml_structured(self, soup):
        structured_elements = []
        discovered_paths = set()

        elements = soup.find_all("Element")
        for elem in elements:
            elem_index = elem.get("Index", "").strip()
            meta_map = {}
            metas = elem.find_all("Metadata")
            for m in metas:
                k = (m.get("Key") or "").strip()
                v = (m.get("Value") or "").strip()
                meta_map[k] = v
                if k:
                    discovered_paths.add(k)
                if v:
                    discovered_paths.add(v)

            structured_elements.append({"index": elem_index, "metadata": meta_map})

        return (structured_elements, list(discovered_paths))

    def _parse_dataasset_xml_fallback(self, soup):
        refs = set()
        for tag in soup.find_all():
            for val in tag.attrs.values():
                if isinstance(val, str):
                    refs.add(val.strip())
            text_content = tag.get_text(strip=True)
            for token in text_content.split():
                refs.add(token.strip())
        return list(refs)

    def _parse_for_data_assets_fallback(self, soup):
        refs = set()
        pattern = re.compile(r"(" + "|".join([re.escape(x) for x in BIG_DUMB_CUP]) + r")$", re.IGNORECASE)
        for tag in soup.find_all():
            for val in tag.attrs.values():
                if isinstance(val, str):
                    candidate = val.strip()
                    if pattern.search(candidate):
                        refs.add(candidate)
            text_content = tag.get_text(strip=True)
            for token in text_content.split():
                if pattern.search(token):
                    refs.add(token.strip())
        return list(refs)

    def _copy_data_assets(self, refs, extracted_root):
        results = []
        if not os.path.isdir(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

        file_map = {}
        for root, _, files in os.walk(extracted_root):
            for filename in files:
                file_map[filename.lower()] = os.path.join(root, filename)

        for ref in refs:
            base = os.path.basename(ref).lower()
            if base in file_map:
                src_path = file_map[base]

                # rename duplicates
                base_name_no_ext, ext = os.path.splitext(os.path.basename(src_path))
                unique_filename = os.path.basename(src_path)
                counter = 1
                while os.path.exists(os.path.join(self.output_dir, unique_filename)):
                    unique_filename = f"{base_name_no_ext}_{counter}{ext}"
                    counter += 1

                dst_path = os.path.join(self.output_dir, unique_filename)

                try:
                    shutil.copy2(src_path, dst_path)
                    h = self._compute_hashes(dst_path)
                    mtype = self._get_mime_type(dst_path)
                    results.append(
                        {
                            "reference": ref,
                            "original_path": src_path,
                            "copied_path": dst_path,
                            "md5": h["md5"],
                            "sha1": h["sha1"],
                            "sha256": h["sha256"],
                            "mime_type": mtype,
                        }
                    )
                except Exception as ex:
                    pass
        return results

    def ppkg_analyze(self):
        try:
            mime_check = self._get_mime_type(self.ppkg_path)
            if mime_check != "application/x-ms-wim":
                self.final_report.clear()
                self.final_report["error"] = f"Incorrect MIME type: {mime_check}"
                return self.final_report

            with tempfile.TemporaryDirectory() as tmpdir:
                try:
                    self._extract_with_7z(tmpdir)
                except subprocess.CalledProcessError as e:
                    self.final_report.clear()
                    self.final_report["error"] = f"7-Zip extraction failed: {e}"
                    return self.final_report

                target_files = []
                for root, _, files in os.walk(tmpdir):
                    for f in files:
                        lf = f.lower()
                        if lf.endswith(".xml") or lf.endswith(".provxml"):
                            target_files.append(os.path.join(root, f))

                all_cmds = []
                all_asset_refs = []
                file_details = []
                found_pkg_config = False

                for xml_path in target_files:
                    try:
                        with open(xml_path, "r", encoding="utf-8") as fh:
                            soup = BeautifulSoup(fh, "xml")
                    except Exception as ex:
                        continue

                    if not found_pkg_config:
                        pcfg = self._parse_package_config(soup)
                        if pcfg:
                            self.final_report["ppkgMetadata"] = pcfg
                            found_pkg_config = True

                    cmds = self._parse_for_commands(soup)
                    all_cmds.extend(cmds)

                    data_refs = []
                    structured_data_assets = []

                    elements_tag = soup.find("Elements", {"Type": "DataAsset"})
                    if elements_tag:
                        s_elements, s_paths = self._parse_dataasset_xml_structured(soup)
                        structured_data_assets = s_elements
                        fallback_refs = self._parse_dataasset_xml_fallback(soup)
                        combined = set(s_paths).union(set(fallback_refs))
                        data_refs = list(combined)
                    else:
                        data_refs = self._parse_for_data_assets_fallback(soup)

                    all_asset_refs.extend(data_refs)

                    file_details.append(
                        {
                            "filePath": xml_path,
                            "commands": cmds,
                            "structuredDataAssets": structured_data_assets,
                            "dataAssetReferences": data_refs,
                        }
                    )

                self.final_report["commands"] = sorted(set(all_cmds))
                self.final_report["fileDetails"] = file_details
                unique_refs = list(set(all_asset_refs))
                copied = self._copy_data_assets(unique_refs, tmpdir)
                self.final_report["copiedDataAssets"] = copied

            return self.final_report

        except Exception as ex:
            error_str = str(ex)[:200]  # limit length
            self.final_report.clear()
            self.final_report["error"] = f"Unexpected error: {error_str}"
            return self.final_report


def main():
    parser = argparse.ArgumentParser(description="https://www.youtube.com/watch?v=7xzU9Qqdqww")
    parser.add_argument("-i", required=True, help="Path to the PPKG file", dest="ppkg")
    parser.add_argument("-d", required=True, help="Directory to copy data assets", dest="output_dir")
    parser.add_argument("-j", help="Optional JSON output file", dest="json_file")
    args = parser.parse_args()

    analyzer = PpkgPursuitOfHappiness(args.ppkg, args.output_dir, args.json_file)
    result = analyzer.ppkg_analyze()

    json_str = json.dumps(result, indent=4)
    print(json_str)

    if args.json_file:
        try:
            with open(args.json_file, "w", encoding="utf-8") as jf:
                jf.write(json_str)
        except Exception as ex:
            print(f"Failed to write JSON to {args.json_file}: {ex}", file=sys.stderr)


if __name__ == "__main__":
    main()
