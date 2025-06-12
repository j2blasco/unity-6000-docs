* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-enablePreprocessing.html

#  [Joint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.html).enablePreprocessing
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
enablePreprocessing; 
### Description
Toggle preprocessing for this joint.
This flag has a connection with rigidbodies that have some of their rotational degrees of freedom frozen. The common example is a 2D game that uses 3D rigidbodies with some of their translational and rotational degrees of freedom frozen.  
  
Rigidbody rotations freezing is internally implemented by setting an infinite inertia around those frozen axes so that the body does not rotate because it's very resistant to.  
  
This approach has some nice properties: most significantly it lets such bodies to correctly go to sleep as opposed to the approach where we would cancel out the rotations around the frozen axes as a post-solver step.  
  
However the downside is that very stiff solver constraints can be generated when such bodies are connected with joints. When the flag is set, PhysX would ignore constraints that produce huge impulses generating only a small change in velocity.  
  
Whilst it may reduce the overall accuracy of the joint simulation, it's been proven to help with overconstrained configurations like in the 2D case. 
* * *
