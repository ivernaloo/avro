import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

import json 
def main():
  """Start of execution"""
  #combine the schemas 
  known_schemas = avro.schema.Names()
  types_schema = LoadAvsc("parameter_types.avsc", known_schemas)
  param_schema = LoadAvsc("parameter.avsc", known_schemas)
  print json.dumps(param_schema.to_json(avro.schema.Names()), indent=2) 
  #test the schema works 
  param_file = open("parameters.avro", "w")
  writer = DataFileWriter(param_file, DatumWriter(), param_schema)
  param_1 = {"name": "test", "description":"An Avro test.", "type":"int"}
  param_2 = {"name": "test", "description":"An Avro test.", "type":"boolean"}
  writer.append(param_1)
  writer.append(param_2)
  writer.close()
  reader = DataFileReader(open("parameters.avro", "r"), DatumReader())
  for parameter in reader:
      print parameter
  reader.close()  
def LoadAvsc(file_path, names=None):
  """Load avsc file
    file_path: path to schema file
    names(optional): avro.schema.Names object
  """
  file_text = open(file_path).read() 
  json_data = json.loads(file_text)
  schema = avro.schema.make_avsc_object(json_data, names) 
  return schema 
if __name__ == "__main__":
  main()