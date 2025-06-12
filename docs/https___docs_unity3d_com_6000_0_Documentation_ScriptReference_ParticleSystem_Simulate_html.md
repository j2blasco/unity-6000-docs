* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Simulate.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).Simulate
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
public void Simulate(float t); 
## Declaration
public void Simulate(float t, bool withChildren = true); 
## Declaration
public void Simulate(float t, bool withChildren = true, bool restart = true); 
## Declaration
public void Simulate(float t, bool withChildren = true, bool restart = true, bool fixedTimeStep = true); 
### Parameters
Parameter | Description  
---|---  
t | Time period in seconds to advance the ParticleSystem simulation by. If `restart` is true, the ParticleSystem will be reset to 0 time, and then advanced by this value. If `restart` is false, the ParticleSystem simulation will be advanced in time from its current state by this value.  
withChildren | Fast-forward all child Particle Systems as well.  
restart | Restart and start from the beginning.  
fixedTimeStep | Only update the system at fixed intervals, based on the value in "Fixed Time" in the Time options.  
### Description
Fast-forwards the Particle System by simulating particles over the given period of time, then pauses it.
Additional resources: [Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Play.html), [Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Pause.html) functions.
* * *
