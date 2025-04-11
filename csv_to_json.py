import pandas as pd
import json
import argparse
import sys
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert CSV file to JSON format')
    parser.add_argument('-i', '--input', 
                        type=str,
                        default='data/arabica_data_cleaned.csv',
                        help='Input CSV file path (default: data/arabica_data_cleaned.csv)')
    parser.add_argument('-o', '--output',
                        type=str,
                        help='Output JSON file path (default: same as input with .json extension)')
    parser.add_argument('--indent',
                        type=int,
                        default=4,
                        help='JSON indentation level (default: 4)')
    return parser.parse_args()

def convert_csv_to_json(input_path, output_path, indent):
    try:
        # Read the CSV file
        df = pd.read_csv(input_path)
        
        # Remove the "Unnamed: 0" column if it exists
        if "Unnamed: 0" in df.columns:
            df = df.drop("Unnamed: 0", axis=1)
        
        # Convert DataFrame to JSON
        json_data = df.to_dict(orient='records')
        
        # Write to JSON file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=indent, ensure_ascii=False)
            
        print(f"Success: CSV file has been converted to JSON and saved as {output_path}")
        return True
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return False

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    # Set output path if not specified
    output_path = args.output
    if output_path is None:
        output_path = str(input_path.with_suffix('.json'))
    
    # Convert CSV to JSON
    success = convert_csv_to_json(str(input_path), output_path, args.indent)
    if not success:
        sys.exit(1)

if __name__ == '__main__':
    main() 