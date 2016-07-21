# AVRO

研究了两种方案 python 和 JS

## Requirement

Linux环境上的安装


    import avro.schema


## Node版本

### Avro-js

Pure JavaScript implementation of the [Avro specification](https://avro.apache.org/docs/current/spec.html).


### Features

+ Fast! Typically twice as fast as JSON with much smaller encodings.
+ Full Avro support, including recursive schemas, sort order, and evolution.
+ Serialization of arbitrary JavaScript objects via logical types.
+ Unopinionated 64-bit integer compatibility.
+ No dependencies, `avro-js` even runs in the browser.


### Installation

```bash
$ npm install avro-js
```

`avro-js` is compatible with all versions of [node.js][] since `0.11` and major
browsers via [browserify][].


### Documentation

See `doc/` folder.


### Examples

Inside a node.js module, or using browserify:

```js
var avro = require('avro-js');
```

+ Encode and decode objects:

```javascript
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
var buf = type.toBuffer(pet); // Serialized object. 显示结果为<Buffer 00 0c 41 6c 62 65 72 74>
var obj = type.fromBuffer(buf); // Pet { kind: 'CAT', name: 'Albert' }
```

+ Generate random instances of a schema:

```javascript
// We can also parse a JSON-stringified schema:
var type = avro.parse('{"type": "fixed", "name": "Id", "size": 4}');
var id = type.random(); // 显示结果. <Buffer d3 7d ab 09>

```

+ Check whether an object fits a given schema:

```javascript
// Or we can specify a path to a schema file (not in the browser):
// .avsc是schema的模式文件
var type = avro.parse('./Person.avsc');
var person = {name: 'Bob', address: {city: 'Cambridge', zip: '02139'}};
var status = type.isValid(person); // Boolean status.
```

+ Get a [readable stream][readable-stream] of decoded records from an Avro
  container file (not in the browser):

```javascript
  // .avro是avro是最后序列化的文件
avro.createFileDecoder('./records.avro')
  .on('metadata', function (type) { /* `type` is the writer's type. */ })
  .on('data', function (record) { /* Do something with the record. */ });
```


[node.js]: https://nodejs.org/en/
[readable-stream]: https://nodejs.org/api/stream.html#stream_class_stream_readable
[browserify]: http://browserify.org/



-----
## Problem
