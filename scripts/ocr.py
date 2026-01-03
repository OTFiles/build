#!/usr/bin/env python3
import base64
import requests
import json
import sys

def process_image(image_path, output_path):
    """Process a single image with OCR.space API"""
    try:
        # Read and encode image
        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')

        # Call OCR.space API (free tier)
        url = 'https://api.ocr.space/parse/image'
        payload = {
            'base64Image': f'data:image/jpeg;base64,{image_data}',
            'language': 'chs',  # Chinese Simplified
            'isOverlayRequired': False,
            'scale': True,
            'detectOrientation': True,
            'OCREngine': 2  # Use OCR Engine 2 for better accuracy
        }

        print(f"Calling OCR.space API for {image_path}...")
        response = requests.post(url, data=payload, timeout=30)
        print(f"Response status: {response.status_code}")
        
        # Parse response
        try:
            result = response.json()
        except:
            print(f"Error: Invalid JSON response")
            print(f"Response text: {response.text[:1000]}")
            return False

        print(f"Response type: {type(result)}")
        
        # Extract text from response
        if isinstance(result, dict):
            if result.get('IsErroredOnProcessing', False):
                print(f"Error: {result.get('ErrorMessage', 'Unknown error')}")
                return False

            ocr_text = result.get('ParsedText', '')
        else:
            print(f"Error: Unexpected response type")
            print(f"Response: {str(result)[:500]}")
            return False

        # Save result
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(ocr_text)

        print(f"Saved: {output_path}")
        return True
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ocr.py <input_image> <output_file>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_file = sys.argv[2]

    success = process_image(input_image, output_file)
    sys.exit(0 if success else 1)