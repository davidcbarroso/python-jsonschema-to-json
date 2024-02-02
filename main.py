import json
import random
import string

def generate_data_from_schema(json_schema):
    try:
        schema = json.loads(json_schema)
    except json.JSONDecodeError as e:
        print(f"Erro no JSON Schema: {e}")
        return

    def generate_data_for_type(data_type):
        if data_type == "string":
            return ''.join(random.choice(string.ascii_letters) for _ in range(10))
        elif data_type == "number":
            return random.uniform(1, 100)
        elif data_type == "integer":
            return random.randint(1, 100)
        elif data_type == "boolean":
            return random.choice([True, False])
        elif data_type == "array":
            return [generate_data_for_type(schema["items"]["type"]) for _ in range(random.randint(1, 5))]
        elif data_type == "object":
            return {field: generate_data_for_type(field_schema["type"]) for field, field_schema in schema.get("properties", {}).items()}
        else:
            return None

    generated_data = generate_data_for_type("object")
    print(json.dumps(generated_data, indent=2))

# Exemplo de uso
json_schema = '''
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/product.schema.json",
  "title": "Product",
  "description": "A product from Acme's catalog",
  "type": "object",
  "properties": {
    "productId": {
      "description": "The unique identifier for a product",
      "type": "integer"
    },
    "productName": {
      "description": "Name of the product",
      "type": "string"
    }
  }
}
'''

generate_data_from_schema(json_schema)
