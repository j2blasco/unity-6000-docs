* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve.html

# WheelFrictionCurve
struct in UnityEngine
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
WheelFrictionCurve is used by the [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html) to describe friction properties of the wheel tire.
The curve takes a measure of tire slip as an input and gives a force as output. The curve is approximated by a two-piece spline. The first section goes from _(0,0)_ to _(extremumSlip,extremumValue)_ , at which point the curve's tangent is zero. The second section goes from _(extremumSlip,extremumValue)_ to _(asymptoteSlip,asymptoteValue)_ , where curve's tangent is again zero:  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/WheelFrictionCurve.png)  
  
Wheel collider computes friction separately from the rest of physics engine, using a slip based friction model. It separates the overall friction force into a "forwards" component (in the direction of rolling, and responsible for acceleration and braking) and "sideways" component (orthogonal to rolling, responsible for keeping the car oriented). Tire friction is described separately in these directions using [WheelCollider.forwardFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-forwardFriction.html) and [WheelCollider.sidewaysFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-sidewaysFriction.html). In both directions it is first determined how much the tire is slipping (what is the speed difference between the rubber and the road). Then this slip value is used to find out tire force exerted on the contact.  
  
The property of real tires is that for low slip they can exert high forces as the rubber compensates for the slip by stretching. Later when the slip gets really high, the forces are reduced as the tire starts to slide or spin. Thus tire friction curves have a shape like in the image above.  
  
Because the friction for the tires is computed separately, the [PhysicsMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial.html) of the ground does not affect the wheels. Simulation of different road materials is done by changing the [WheelCollider.forwardFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-forwardFriction.html) and [WheelCollider.sidewaysFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-sidewaysFriction.html) of the wheel, based on what material the wheel is hitting.  
  
Additional resources: [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html), [WheelCollider.forwardFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-forwardFriction.html), [WheelCollider.sidewaysFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-sidewaysFriction.html).
### Properties
Property | Description  
---|---  
[asymptoteSlip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-asymptoteSlip.html) | Asymptote point slip (default 2).  
[asymptoteValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-asymptoteValue.html) | Force at the asymptote slip (default 10000).  
[extremumSlip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-extremumSlip.html) | Extremum point slip (default 1).  
[extremumValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-extremumValue.html) | Force at the extremum slip (default 20000).  
[stiffness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-stiffness.html) | Multiplier for the extremumValue and asymptoteValue values (default 1).  
* * *
