* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.ConfigureVehicleSubsteps.html

#  [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html).ConfigureVehicleSubsteps
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html "Go to WheelCollider Component in the Manual")
## Declaration
public void ConfigureVehicleSubsteps(float speedThreshold, int stepsBelowThreshold, int stepsAboveThreshold); 
### Parameters
Parameter | Description  
---|---  
speedThreshold | The speed threshold of the sub-stepping algorithm.  
stepsBelowThreshold | Amount of simulation sub-steps when vehicle's speed is below speedThreshold.  
stepsAboveThreshold | Amount of simulation sub-steps when vehicle's speed is above speedThreshold.  
### Description
Configure vehicle sub-stepping parameters.
Every time a fixed update happens, the vehicle simulation splits this fixed delta time into smaller sub-steps and calculates suspension and tire forces per each smaller delta. Then, it would sum up all resulting forces and torques, integrate them, and apply to the vehicle's body.  
  
Using this function you can customize how many sub-steps will be performed by the simulation above and below the speed threshold.  
  
It's enough to call this function only once per each vehicle, as it actually sets parameters to the vehicle but not to a wheel.
* * *
