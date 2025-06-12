* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.TryLoad.html

#  [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).TryLoad
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
public bool TryLoad(ref [Search.PropertyDatabaseRecordKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey.html) recordKey, out object value); 
### Parameters
Parameter | Description  
---|---  
recordKey | A record key.  
value | The property value.  
### Returns
**bool** True if the record is found and is valid, false otherwise. 
### Description
Loads a single property, already deseriazed into an object.
```
// Load the value already deserialized.
var colorRecordKey = PropertyDatabase.CreateRecordKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateRecordKey.html)("path/to/my/asset", "m_Color");
if (!propertyDatabase.TryLoad(colorRecordKey, out object colorObject))
    Assert.Fail("Failed to load color property.");
var color = (Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html))colorObject;
Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(1, 0, 1), color);

```

Additional resources: [PropertyDatabase.CreateRecordKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateRecordKey.html).
* * *
## Declaration
public bool TryLoad(ref [Search.PropertyDatabaseRecordKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey.html) recordKey, out [Search.IPropertyDatabaseRecordValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IPropertyDatabaseRecordValue.html) value); 
### Parameters
Parameter | Description  
---|---  
recordKey | A record key.  
value | The property record.  
### Returns
**bool** True if the record is found and is valid, false otherwise. 
### Description
Loads a single property, still contained within a record.
This method doesn't deserialize the value. You have to deserialize it yourself by calling [PropertyDatabase.GetObjectFromRecordValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.GetObjectFromRecordValue.html).
```
// Load the record value to do a deserialization at the appropriate time.
var sizeRecordKey = PropertyDatabase.CreateRecordKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateRecordKey.html)("path/to/my/asset", "m_Size");
if (!propertyDatabase.TryLoad(sizeRecordKey, out IPropertyDatabaseRecordValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IPropertyDatabaseRecordValue.html) sizeRecordValue))
    Assert.Fail("Failed to load size property.");
var size = propertyDatabase.GetValueFromRecord<int>(sizeRecordValue);
Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(42, size);

```

Additional resources: [PropertyDatabase.CreateRecordKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateRecordKey.html).
* * *
## Declaration
public bool TryLoad(ulong documentKey, out IEnumerable<object> data); 
### Parameters
Parameter | Description  
---|---  
documentKey | A document key.  
data | The document property values.  
### Returns
**bool** True if the record is found and is valid, false otherwise. 
### Description
Loads all the properties of a document, already deseriazed into objects.
```
// Load all values not associated with a document, already deserialized.
var nullDocumentKey = PropertyDatabase.CreateDocumentKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateDocumentKey.html)(null);
if (!propertyDatabase.TryLoad(nullDocumentKey, out IEnumerable<object> noDocumentProperties))
    Assert.Fail("Failed to load properties with no documents.");
Assert.IsNotEmpty(noDocumentProperties);
Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)("myDocs_", noDocumentProperties.First());

```

Additional resources: [PropertyDatabase.CreateDocumentKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateDocumentKey.html).
* * *
## Declaration
public bool TryLoad(ulong documentKey, out IEnumerable<IPropertyDatabaseRecord> records); 
### Parameters
Parameter | Description  
---|---  
documentKey | A document key.  
records | The document property records.  
### Returns
**bool** True if the record is found and is valid, false otherwise. 
### Description
Loads all the properties of a document, still contained within records.
This method doesn't deserialize the values. You have to deserialize them yourself by calling [PropertyDatabase.GetObjectFromRecordValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.GetObjectFromRecordValue.html).
```
// Load all values associated with a document, not deserialized.
var myAssetDocumentKey = PropertyDatabase.CreateDocumentKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateDocumentKey.html)("path/to/my/asset");
if (!propertyDatabase.TryLoad(myAssetDocumentKey, out IEnumerable<IPropertyDatabaseRecord[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IPropertyDatabaseRecord.html)> myDocumentRecords))
    Assert.Fail("Failed to load records for my asset document.");
var deserializedValues = new Dictionary<PropertyDatabaseRecordKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey.html), object>();
foreach (var myDocumentRecord in myDocumentRecords)
{
    var value = propertyDatabase.GetValueFromRecord<object>(myDocumentRecord.value);
    deserializedValues.Add(myDocumentRecord.key, value);
}
Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(5, deserializedValues.Count);

```

Additional resources: [PropertyDatabase.CreateDocumentKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateDocumentKey.html).
* * *
