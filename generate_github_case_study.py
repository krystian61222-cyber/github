#!/usr/bin/env python3
"""Generate the complete GitHub a16z case study .docx file."""

import sys
import os

# Ensure the script's directory is in path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gen_part1 import create_doc, build_sections_1_to_3
from gen_part2 import build_sections_4_to_5
from gen_part3 import build_section_6
from gen_part4 import build_sections_7_to_8
from gen_part5 import build_section_9
from gen_part6 import build_section_10_and_bibliography


def main():
    doc = create_doc()
    build_sections_1_to_3(doc)
    build_sections_4_to_5(doc)
    build_section_6(doc)
    build_sections_7_to_8(doc)
    build_section_9(doc)
    build_section_10_and_bibliography(doc)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'GitHub_a16z_case_study.docx')
    doc.save(output_path)
    print(f'Document saved to: {output_path}')


if __name__ == '__main__':
    main()
