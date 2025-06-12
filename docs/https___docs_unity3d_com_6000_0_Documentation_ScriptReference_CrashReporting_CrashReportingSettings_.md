* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReporting.CrashReportingSettings-logBufferSize.html

#  [CrashReportingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReporting.CrashReportingSettings.html).logBufferSize
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
logBufferSize; 
### Description
The Performance Reporting service will keep a buffer of up to the last X log messages (Debug.Log, etc) to send along with crash reports. The default is 10 log messages, the max is 50. Set this to 0 to disable capture of logs with your crash reports.
* * *
