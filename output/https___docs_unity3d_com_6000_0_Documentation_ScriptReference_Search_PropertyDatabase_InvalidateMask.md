* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.InvalidateMask.html

#  [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).InvalidateMask
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
public void InvalidateMask(ulong documentKeyMask); 
### Parameters
Parameter | Description  
---|---  
documentKeyMask | A document key mask.  
### Description
Invalidate all properties stored from multiple documents that match a document key mask.
This operation is slower than the simpler [PropertyDatabase.Invalidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.Invalidate.html) since we cannot rely on a binary search to find all keys that match the mask.
```
// Store properties of multiple documents.
for (ulong i = 0; i < 10; ++i)
{
    for (var j = 0; j < 10; ++j)
        propertyDatabase.Store(i, PropertyDatabase.CreatePropertyHash[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreatePropertyHash.html)($"prop{j}"), $"value{j}");
}
// Invalidate all documents that match any set bits of the mask.
ulong invalidatedDocumentMask = 2;
propertyDatabase.InvalidateMask(invalidatedDocumentMask);

// The invalidated documents can no longer be retrieved.
for (ulong i = 0; i < 10; ++i)
{
    if ((i & invalidatedDocumentMask) == 0)
        continue;
    if (propertyDatabase.TryLoad(i, out IEnumerable<object> invalidatedDocumentValues))
        Assert.Fail("TryLoad should have failed to retrieve the invalidated document values.");
}

```

Additional resources: [PropertyDatabase.CreateDocumentKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateDocumentKey.html).
* * *
