* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.ClearCompletedMetrics.html

#  [AsyncReadManagerMetrics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html).ClearCompletedMetrics
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
public static void ClearCompletedMetrics(); 
### Description
Clears the metrics for all completed requests, including failed and canceled requests.
You can also clear metrics data when you call [GetMetrics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html) or [GetCurrentSummaryMetrics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetCurrentSummaryMetrics.html) by passing in the appropriate AsyncReadManager.Flags. Consider how and when you clear metrics data. You want to avoid collecting duplicate metrics records, but you also want to avoid deleting data you haven’t accessed yet. Avoid calling this function from more than one place in your application. For example, if you had two classes attempting to measure these metrics independently, clearing the data in one class would interfere with the other since all the metrics for completed read requests are removed.
* * *
