* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.IndexNumber.html

#  [ObjectIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html).IndexNumber
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
public void IndexNumber(int documentIndex, string name, double number); 
### Parameters
Parameter | Description  
---|---  
documentIndex | Document where the indexed value was found.  
name | Key used to retrieve the value.  
number | Number value to store in the index.  
### Description
Adds a key-number value pair to the index. The key won't be added with variations.
The following example uses `IndexNumber` to index a number `testsize` property that can be searched using common number operators such as `>=`, i.e. `testsize>=4.2`. 
```
[CustomObjectIndexer(typeof(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)), version = 3)]
static void IndexObjectSize(CustomObjectIndexerTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) target, ObjectIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) indexer)
{
    var collider = target.target as Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html);
    if (collider == null)
        return;

    var totalSize = CustomSelectors.ComputeColliderSize(collider);
    indexer.IndexNumber(target.documentIndex, "collidersize", totalSize);
}

```

* * *
