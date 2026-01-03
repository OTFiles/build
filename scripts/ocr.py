#!/usr/bin/env python3
import base64
import json
import subprocess
import sys
import os

def process_image(image_path, output_path):
    """Process a single image with Umi-OCR"""
    try:
        # Read and encode image
        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')

        # Create request
        request = {
            "base64": image_data,
            "options": {
                "tbpu.parser": "multi_para"
            }
        }

        # Save request to file
        with open('/tmp/request.json', 'w', encoding='utf-8') as f:
            json.dump(request, f, ensure_ascii=False)

        # Call API
        result = subprocess.run([
            'curl', '-s', '-X', 'POST', 'http://localhost:1224/api/ocr',
            '-H', 'Content-Type: application/json',
            '-d', '@/tmp/request.json'
        ], capture_output=True, text=True)

        # Parse response
        try:
            response = json.loads(result.stdout)
            ocr_text = response.get('data', '')
        except:
            ocr_text = ''

        # Save result
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(ocr_text)

        print(f"Saved: {output_path}")
        return True
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ocr.py <input_image> <output_file>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_file = sys.argv[2]

    success = process_image(input_image, output_file)
    sys.exit(0 if success else 1)