* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Clear.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).Clear
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html "Go to ParticleSystem Component in the Manual")
## Declaration
public void Clear(); 
## Declaration
public void Clear(bool withChildren = true); 
### Parameters
Parameter | Description  
---|---  
withChildren | Clear all child Particle Systems as well.  
### Description
Remove all particles in the Particle System.
This method also removes the particles from any linked sub-emitters. Use the withChildren parameter to remove particles from child Particle Systems that are not sub-emitters of the system.
* * *
