* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory-ctor.html

# ProfilerCategory Constructor
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
public ProfilerCategory(string categoryName); 
### Parameters
Parameter | Description  
---|---  
categoryName | Profiler category name.  
### Description
Use to construct ProfilerCategory by category name.
This constructor performs a lookup across built-in Profiler categories and stores the category identifier. If the category does not exist, then it uses [ProfilerCategory.Scripts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Scripts.html) instead.
* * *
