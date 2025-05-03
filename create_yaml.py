import yaml
import re
from datetime import datetime
from zoneinfo import ZoneInfo

def extract_lua_dict(lua_file):
    """
    Extracts auto translates and items from a Lua file and returns a dictionary
    """
    pattern = re.compile(r'\[(\d+)\]\s*=\s*{[^}]*?id=\1[^}]*?ja="([^"]+)"')
    lua_dict = {}
    
    try:
        with open(lua_file, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = pattern.findall(content)
            for id_str, ja_str in matches:
                lua_dict[int(id_str)] = ja_str
    except Exception as e:
        print(f"Error loading Lua file '{lua_file}': {e}")
    
    return lua_dict

def save_dict_to_yaml(dictionary, output_file):
    """
    Save the dictionary as a YAML file
    """
    jst = ZoneInfo("Asia/Tokyo")
    timestamp = datetime.now(jst).strftime('%Y-%m-%d %H:%M:%S')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {timestamp}\n")
        yaml.dump(dictionary, f, allow_unicode=True, sort_keys=False)

def main():
    auto_translates_lua = 'resources_data/auto_translates.lua'
    items_lua = 'resources_data/items.lua'
    auto_translates_output = 'data/auto_translates.yaml'
    items_output = 'data/items.yaml'

    auto_translates_dict = extract_lua_dict(auto_translates_lua)
    items_dict = extract_lua_dict(items_lua)

    save_dict_to_yaml(auto_translates_dict, auto_translates_output)
    save_dict_to_yaml(items_dict, items_output)

if __name__ == '__main__':
    main()
