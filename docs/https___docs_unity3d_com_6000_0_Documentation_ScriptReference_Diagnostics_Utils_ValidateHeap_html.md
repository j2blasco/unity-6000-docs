* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.Utils.ValidateHeap.html

#  [Utils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.Utils.html).ValidateHeap
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
public static void ValidateHeap(); 
### Description
Scans the managed heap to check for corrupted objects.
This function only works when you use the Mono scripting backend. If this function discovers a corrupted object, the editor log displays a callstack and the Editor crashes, either through a fatal native assert or an access violation within Mono. Use this function to find memory corruption closer to when it occurs.
* * *
