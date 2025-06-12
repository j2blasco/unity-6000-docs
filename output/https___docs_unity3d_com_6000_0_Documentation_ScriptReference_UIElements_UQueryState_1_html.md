* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.html

# UQueryState<T0>
struct in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
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
Query object containing all the selection rules. The object can be saved and rerun later without re-allocating memory. 
### Public Methods
Method | Description  
---|---  
[AtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.AtIndex.html) |  Selects the nth element matching all the criteria, or null if not enough elements were found.   
[First](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.First.html) |  The first element matching all the criteria, or null if none was found.   
[ForEach](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.ForEach.html) |  Invokes function on all elements matching the query.   
[GetEnumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.GetEnumerator.html) |  Allows traversing the results of the query with foreach without creating GC allocations.   
[Last](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.Last.html) |  The last element matching all the criteria, or null if none was found.   
[RebuildOn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.RebuildOn.html) |  Creates a new QueryState with the same selection rules, applied on another VisualElement.   
[ToList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.ToList.html) |  Adds all elements satisfying selection rules to the list.   
* * *
