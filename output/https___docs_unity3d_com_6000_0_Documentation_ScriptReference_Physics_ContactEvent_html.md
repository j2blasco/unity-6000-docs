* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ContactEvent.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).ContactEvent
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
### Parameters
Parameter | Description  
---|---  
value | A delegate to call.  
### Description
Subscribe to this event to read all collisions that occurred during the physics simulation step.
Each subscriber to this event gets invoked with a physics scene and a native array of [ContactPairHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader.html)s. Each [ContactPairHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader.html) contains an array of [ContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair.html)s and each [ContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair.html) contains an array of [ContactPairPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairPoint.html)s.  
  
You can use this event to speed up contact processing as it's a lot faster than [MonoBehaviour.OnCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionEnter.html) and other messages. You can also use this event to schedule jobs that use the provided native array. Jobs that are scheduled from this event must be completed before the next [Physics.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Simulate.html), [PhysicsScene.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.Simulate.html), or [PhysicsScene.RunSimulationStages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.RunSimulationStages.html) with the [RunSimulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationStage.RunSimulation.html) stage call. By default a good place to complete these jobs is [MonoBehaviour.FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html).  
  
Notes: 
  * Only Collider collisions are reported in this event and no trigger events will appear in the provided buffer.
  * All the data in the provided buffer is read-only. No writes are permited.
  * The event is invoked after the transform sync.
  * To receive contacts from a Collider, set the [Collider.providesContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-providesContacts.html) property to `true` or attach a [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) script with an OnCollisionStay method.


```
using System.Collections.Generic;
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;  
  
public class BounceScipt : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private float m_ImpulseMultiplier = 5f;  
  
    private struct JobResultStruct
    {
        public int thisInstanceID;
        public int otherInstanceID;
        public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) averageNormal;
    }  
  
    private NativeArray<JobResultStruct> m_ResultsArray;
    private int m_Count;
    private JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) m_JobHandle;  
  
    private readonly Dictionary<int, Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)> m_RigidbodyMapping = new Dictionary<int, Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
    private void OnEnable()
    {
        m_ResultsArray = new NativeArray<JobResultStruct>(16, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));  
  
        Physics.ContactEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ContactEvent.html) += Physics_ContactEvent;  
  
        var allRBs = GameObject.FindObjectsOfType<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        foreach (var rb in allRBs)
            m_RigidbodyMapping.Add(rb.GetInstanceID(), rb);
    }  
  
    private void OnDisable()
    {
        m_JobHandle.Complete();
        m_ResultsArray.Dispose();  
  
        Physics.ContactEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ContactEvent.html) -= Physics_ContactEvent;  
  
        m_RigidbodyMapping.Clear();
    }  
  
    private void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        m_JobHandle.Complete(); // The buffer is valid until the next Physics.Simulate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Simulate.html)() call. Be it internal or manual  
  
        // Do something with the contact data.
        // E.g. Add force based on the average contact normal for that body
        for (int i = 0; i < m_Count; i++)
        {
            var thisInstanceID = m_ResultsArray[i].thisInstanceID;
            var otherInstanceID = m_ResultsArray[i].otherInstanceID;  
  
            var rb0 = thisInstanceID != 0 ? m_RigidbodyMapping[thisInstanceID] : null;
            var rb1 = otherInstanceID != 0 ? m_RigidbodyMapping[otherInstanceID] : null;  
  
            if (rb0)
                rb0.AddForce(m_ResultsArray[i].averageNormal * m_ImpulseMultiplier, ForceMode.Impulse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html));
            if (rb1)
                rb1.AddForce(m_ResultsArray[i].averageNormal * -m_ImpulseMultiplier, ForceMode.Impulse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html));
        }
    }  
  
    private void Physics_ContactEvent(PhysicsScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) scene, NativeArray<ContactPairHeader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader.html)>.ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html) pairHeaders)
    {
        int n = pairHeaders.Length;  
  
        if (m_ResultsArray.Length < n)
        {
            m_ResultsArray.Dispose();
            m_ResultsArray = new NativeArray<JobResultStruct>(Mathf.NextPowerOfTwo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html)(n), Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
        }  
  
        m_Count = n;  
  
        AddForceJob job = new AddForceJob()
        {
            pairHeaders = pairHeaders,
            resultsArray = m_ResultsArray
        };  
  
        m_JobHandle = job.Schedule(n, 256);
    }  
  
    private struct AddForceJob : IJobParallelFor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelFor.html)
    {
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public NativeArray<ContactPairHeader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader.html)>.ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html) pairHeaders;  
  
        public NativeArray<JobResultStruct> resultsArray;  
  
        public void Execute(int index)
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) averageNormal = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
            int count = 0;  
  
            for (int j = 0; j < pairHeaders[index].pairCount; j++)
            {
                ref readonly var pair = ref pairHeaders[index].GetContactPair(j);  
  
                if (pair.IsCollisionExit)
                    continue;  
  
                for (int k = 0; k < pair.ContactCount; k++)
                {
                    ref readonly var contact = ref pair.GetContactPoint(k);
                    averageNormal += contact.Normal;
                }  
  
                count += pair.ContactCount;
            }  
  
            if (count != 0)
                averageNormal /= (float)count;  
  
            JobResultStruct result = new JobResultStruct()
            {
                thisInstanceID = pairHeaders[index].bodyInstanceID,
                otherInstanceID = pairHeaders[index].otherBodyInstanceID,
                averageNormal = averageNormal
            };  
  
            resultsArray[index] = result;
        }
    }
}

```

This script reads all the contacts in the buffer and computes the average normal for each ContactPairHeader. Then applies a force based on the result.
* * *
