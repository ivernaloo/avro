var avro =  require('avro-js');

// We can declare a schema inline:
var type = avro.parse({
    name: 'Pet',
    type: 'record',
    fields: [
        {name: 'kind', type: {name: 'Kind', type: 'enum', symbols: ['CAT', 'DOG']}},
        {name: 'name', type: 'string'}
    ]
});
var pet = {kind: 'CAT', name: 'Albert'};
var buf = type.toBuffer(pet); // Serialized object. <Buffer 00 0c 41 6c 62 65 72 74>
var obj = type.fromBuffer(buf); // {kind: 'CAT', name: 'Albert'}  Pet { kind: 'CAT', name: 'Albert' }

var type2 = avro.parse('{"type": "fixed", "name": "Id", "size": 4}');
var random = type2.random();


console.log("buf : ", buf);
console.log("obj : ", obj);
console.log("random : ", random);
