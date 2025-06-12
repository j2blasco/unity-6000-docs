* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-maximumParticleDeltaTime.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).maximumParticleDeltaTime
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
maximumParticleDeltaTime; 
### Description
The maximum time a frame can spend on particle updates. If the frame takes longer than this, then updates are split into multiple smaller updates.
Use this function to balance the accuracy of particle simulation against your performance target.  
  
Using a small value gives higher quality particle simulations, but takes more processing time. Particle updates run multiple times at smaller time increments, if the frame time exceeds the threshold provided.  
  
Conversely, a higher value ensures that particle simulations are not broken down into multiple steps per frame, giving the best performance, but loses simulation accuracy when using some of the more advanced particle simulation features.
* * *
