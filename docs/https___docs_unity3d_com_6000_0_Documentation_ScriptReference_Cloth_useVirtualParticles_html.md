* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-useVirtualParticles.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).useVirtualParticles
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html "Go to Cloth Component in the Manual")
useVirtualParticles; 
### Description
Add one virtual particle per triangle to improve collision stability.
Virtual particles provide a way of improving cloth collision without increasing the cloth resolution. They are called 'virtual' particles because they only exist during the collision processing stage and do not have their position, velocity or mass explicitly stored like regular particles, they can be thought of as providing additional samples on the collision surface.
* * *
