* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey.html

# PropertyDatabaseRecordKey
struct in UnityEditor.Search
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
### Description
The key of a record that is stored in the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).
A key is a numerical value that represents a description of the property being stored in the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html). It is composed of two parts, the document key and the property key.  
  
The document key represents what document owns the property, and the property key represents the property itself. For example, if you wish to store the size of a file, the file would be the document and the size would be the property. You can use any value for your documents, as long as it is consistent when storing multiple properties of a single document. You can also not use a document, in which case the document key will be 0.  
  
We provide multiple helper functions to help create record keys, see [PropertyDatabase.CreateRecordKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateRecordKey.html), [PropertyDatabase.CreateDocumentKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateDocumentKey.html) and [PropertyDatabase.CreatePropertyHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreatePropertyHash.html).
### Static Properties
Property | Description  
---|---  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey-size.html) | The size of the key, in bytes.  
### Properties
Property | Description  
---|---  
[documentKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey-documentKey.html) | The key of the document owning the property.  
[propertyKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey-propertyKey.html) | The key of the property.  
### Constructors
Constructor | Description  
---|---  
[PropertyDatabaseRecordKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey-ctor.html) | Constructs a new record key.  
### Public Methods
Method | Description  
---|---  
[CompareTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey.CompareTo.html) | Compares the record key to another record key.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey.Equals.html) | Tests equality with another record key.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey.GetHashCode.html) | Gets the hashcode of the key.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey-operator_ne.html) | The not equal operator.  
[operator <](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey-operator_lt.html) | The less than operator.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey-operator_eq.html) | The equals operator.  
[operator >](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey-operator_gt.html) | The greater than operator.  
* * *
