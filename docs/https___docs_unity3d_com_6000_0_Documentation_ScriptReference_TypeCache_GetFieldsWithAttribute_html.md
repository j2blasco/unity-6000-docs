* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TypeCache.GetFieldsWithAttribute.html

#  [TypeCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TypeCache.html).GetFieldsWithAttribute
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
public static [TypeCache.FieldInfoCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TypeCache.FieldInfoCollection.html) GetFieldsWithAttribute(); 
## Declaration
public static [TypeCache.FieldInfoCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TypeCache.FieldInfoCollection.html) GetFieldsWithAttribute(Type attrType); 
## Declaration
public static [TypeCache.FieldInfoCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TypeCache.FieldInfoCollection.html) GetFieldsWithAttribute(string assemblyName); 
## Declaration
public static [TypeCache.FieldInfoCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TypeCache.FieldInfoCollection.html) GetFieldsWithAttribute(Type attrType, string assemblyName); 
### Parameters
Parameter | Description  
---|---  
attrType | Attribute type.  
assemblyName | Optional assembly name.  
### Returns
**FieldInfoCollection** Returns an unordered FieldInfo collection of fields marked with the **T** attribute. If assemblyName is specified, returns only fields defined in this assembly. 
### Description
Retrieves an unordered collection of fields marked with the **T** attribute.
This method provides fast access to all class fields loaded from a given assembly or all Unity domain assemblies and marked with a specific attribute. Fields marked with ancestors of the specified attribute are also included in the result. The order of results is undefined.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;  
  
public class Example
{
    class MyAttribute : Attribute {}  
  
    [MyAttribute]
    static int s_MyField;  
  
    static void ScanStaticFieldsMarkedWithMyAttribute()
    {
        var extractedFields = TypeCache.GetFieldsWithAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TypeCache.GetFieldsWithAttribute.html)<MyAttribute>();
        foreach (var fi in extractedFields)
        {
            if (!fi.IsStatic)
                continue;
            //...
        }
    }
}

```

**Note:** The returned [FieldInfoCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TypeCache.FieldInfoCollection.html) is read-only and thread-safe. The order of FieldInfo in the collection is undefined.
* * *
