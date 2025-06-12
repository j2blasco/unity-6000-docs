* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsMemoryBudget.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).streamingMipmapsMemoryBudget
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
streamingMipmapsMemoryBudget; 
### Description
The total amount of memory (in megabytes) to be used by streaming and non-streaming textures.
Non-streaming textures will always be loaded at the largest mipmap level (even if that exceeds the budget). Streaming textures will pick the smallest mipmap level possible to try to hit the memory budget.
* * *
