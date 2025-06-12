* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.High.html

#  [ManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html).High
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
UnityLinker will strip as much as possible. This will further reduce code size beyond what Medium can achieve. However, this additional reduction may come with tradeoffs. Possible side effects may include, managed code debugging of some methods may no longer work. You may need to maintain a custom link.xml file, and some reflection code paths may not behave the same.
* * *
