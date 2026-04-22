import os

def generate_toc(path, indent=0):
    toc = []
    for item in sorted(os.listdir(path)):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if item.startswith('.'):
                continue
            toc.append("  " * indent + f"- [{item}]({item})")
            toc.extend(generate_toc(item_path, indent + 1))
        elif item.endswith('.md') and item != 'README.md':
            toc.append("  " * indent + f"- [{item[:-3]}]({item})")
    return toc

def main():
    toc = ["# Whacking Infodump", "", "## Table of Contents", ""] + generate_toc('.')
    with open('README.md', 'w') as f:
        f.write('\n'.join(toc))

if __name__ == "__main__":
    main()
