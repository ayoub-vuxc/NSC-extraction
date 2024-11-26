import re

manifest_file_path = "AndroidManifest.xml"

with open(manifest_file_path, 'r', encoding='utf-8') as manifest_file:
    manifest_content = manifest_file.read()

match = re.search(r'android:networkSecurityConfig\s*=\s*[\'"](\S+)[\'"]', manifest_content, re.IGNORECASE)

if match:
    value_after_equals = match.group(1).strip()


    def a():
        return value_after_equals
else:
    print("Pattern not found or no value after 'android:networkSecurityConfig' in the manifest.")

print(a())
