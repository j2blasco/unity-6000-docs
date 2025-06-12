* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Start.html

#  [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).Start
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
public static int Start(string name, string description, [Progress.Options](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.html) options, int parentId); 
### Parameters
Parameter | Description  
---|---  
name | The progress indicator's name. You can display the name as a title in the progress window. Use / (slash) as a separator to group child progress indicators together.  
description | The progress indicator's initial description. You can change it using Report or SetDescription.  
parentId | The unique ID of the parent progress indicator, if any. If the progress indicator has no parent, pass -1.  
options | The progress indicator's initial progress options.  
### Returns
**int** The newly created progress identifier. This identifier is used for all other APIs to update the progress status. 
### Description
This method starts a new progress indicator.
```
public IEnumerator Run_TwoTasks()
{
    var title1 = "Running task 1...";
    var title2 = "Running task 2...";
    int progressId1 = Progress.Start[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Start.html)(title1);
    int progressId2 = Progress.Start[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Start.html)(title2);  
  
    Progress.ShowDetails[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.ShowDetails.html)(false);
    yield return null;  
  
    for (int frame = 0; frame <= 10; ++frame)
    {
        Progress.Report[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Report.html)(progressId1, Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html));
        yield return WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(0.5f);
        Progress.Report[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Report.html)(progressId2, Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html));
        yield return WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(0.5f);
    }  
  
    Progress.Remove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Remove.html)(progressId1);
    Progress.Remove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Remove.html)(progressId2);
}

```

* * *
