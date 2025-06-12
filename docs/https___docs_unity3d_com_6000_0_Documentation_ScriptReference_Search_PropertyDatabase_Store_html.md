* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.Store.html

#  [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).Store
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public bool Store(string documentId, string propertyPath, object value); 
### Parameters
Parameter | Description  
---|---  
documentId | A document identifier.  
propertyPath | A property path or name.  
value | The value of the property.  
### Returns
**bool** True if the store operation succeeded, false if not. 
### Description
Stores a document property.
```
// Store a property of a document, like a property of an asset.
var stored = propertyDatabase.Store("path/to/my/asset", "m_Color", new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(1, 0, 1));
if (!stored)
    Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("Property m_Color did not store.");

```

* * *
## Declaration
public bool Store(ulong documentKey, [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) propertyHash, object value); 
### Parameters
Parameter | Description  
---|---  
documentKey | A document key.  
propertyHash | A property hash.  
value | The value of the property.  
### Returns
**bool** True if the store operation succeeded, false if not. 
### Description
Stores a document property with a precomputed document key and property hash.
```
// Store a property of a document, with the document id and property hash already computed.
var documentId = PropertyDatabase.CreateDocumentKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateDocumentKey.html)("path/to/my/asset");
var propertyHash = PropertyDatabase.CreatePropertyHash[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreatePropertyHash.html)("m_Size");
stored = propertyDatabase.Store(documentId, propertyHash, 42);
if (!stored)
    Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("Property m_Size did not store.");

```

Additional resources: [PropertyDatabase.CreateDocumentKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateDocumentKey.html) and [PropertyDatabase.CreatePropertyHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreatePropertyHash.html).
* * *
## Declaration
public bool Store(ref [Search.PropertyDatabaseRecordKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey.html) recordKey, object value); 
### Parameters
Parameter | Description  
---|---  
recordKey | A record key.  
value | The value of the property.  
### Returns
**bool** True if the store operation succeeded, false if not. 
### Description
Stores a document property with a precomputed record key.
```
// Store a property with an already computed record key.
var recordKey = PropertyDatabase.CreateRecordKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateRecordKey.html)("path/to/my/asset", "prop1");
stored = propertyDatabase.Store(recordKey, 123);
if (!stored)
    Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("Property prop1 did not store.");

```

Additional resources: [PropertyDatabase.CreateRecordKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateRecordKey.html).
* * *
## Declaration
public bool Store([Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) propertyHash, object value); 
### Parameters
Parameter | Description  
---|---  
propertyHash | A property hash.  
value | The value of the property.  
### Returns
**bool** True if the store operation succeeded, false if not. 
### Description
Stores a property with a precomputed property hash.
The document identifier is considered null and the document key will be 0.
```
// Store a property without any document.
stored = propertyDatabase.Store(PropertyDatabase.CreatePropertyHash[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreatePropertyHash.html)("documentPrefix"), "myDocs_");
if (!stored)
    Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("Property documentPrefix did not store.");

```

Additional resources: [PropertyDatabase.CreatePropertyHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreatePropertyHash.html).
* * *
