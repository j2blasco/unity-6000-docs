* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetCustomDiffTool.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).SetCustomDiffTool
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
public static void SetCustomDiffTool(string path, string twoWayDiff, string threeWayDiff, string mergeCommand, bool forceEnableCustomTool); 
### Parameters
Parameter | Description  
---|---  
path | Diff tool path.  
twoWayDiff | Two - way diff command line.  
threeWayDiff | Three - way diff command line.  
mergeCommand | Merge command line.  
forceEnableCustomTool | Sets Custom Tool as current active Revision Control Diff/Merge tool.  
### Description
Set custom diff tool settings.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("SetCustomDiffTool/DiffMerge")]
    public static void ExampleSetCustomDiffTool()
    {
        string path = "/Applications/DiffMerge.app/Contents/MacOS/DiffMerge";
        string twoWayDiffCommandLine = "-t1 #LTITLE -t2 #RTITLE #LEFT #RIGHT";
        string threeWayDiffCommandLine = "-t1 #LTITLE -t2 #ATITLE -t3 #RTITLE -ro2 #LEFT #ANCESTOR #RIGHT";
        string mergeArguments = "-m -t1 #LTITLE -t2 #ATITLE -t3 #RTITLE -r #OUTPUT #LEFT #ANCESTOR #RIGHT";  
  
        EditorUtility.SetCustomDiffTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetCustomDiffTool.html)(path, twoWayDiffCommandLine, threeWayDiffCommandLine, mergeArguments);
    }
}

```

For more information about diff tools, see [ Revision Control Diff/Merge](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html).
* * *
