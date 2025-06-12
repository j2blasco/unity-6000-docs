* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.GIContributorsReceivers.html

#  [DrawCameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.html).GIContributorsReceivers
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
Draw Mesh Renderers and Terrains in different colors to show their [StaticEditorFlags.ContributeGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.ContributeGI.html) / [ReceiveGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.html) properties. With default colors:   
  
Yellow means 'ContributeGI' is off.   
Blue means that 'ContributeGI' is on and the object receives GI from lightmaps. Additional resources: [ReceiveGI.Lightmaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.Lightmaps.html)   
Red means that 'ContributeGI' is on, but that the object receives GI from Light Probes instead. Additional resources: [ReceiveGI.LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.LightProbes.html).  
  
All colors can be adjusted under Preferences > Colors.
* * *
