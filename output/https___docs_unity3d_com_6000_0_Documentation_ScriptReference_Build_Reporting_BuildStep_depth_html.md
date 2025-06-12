* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildStep-depth.html

#  [BuildStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildStep.html).depth
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
depth; 
### Description
The nesting depth of the build step.
The build process is broken down into steps, and steps may themselves be broken down into sub-steps recursively. The nesting depth indicates how many higher-level build steps enclose this step. The step that represents the overall build process has depth 0, the sub-steps of that step have depth 1, and so on.
* * *
