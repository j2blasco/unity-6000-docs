* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GfxThreadingMode.SplitJobs.html

#  [GfxThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GfxThreadingMode.html).SplitJobs
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
Split Graphics Jobs.
Main thread starts worker threads to write Unity graphics commands. Render thread reads Unity graphics commands converts them to native graphics commands. The render thread also starts worker threads to write native graphics commands.
* * *
