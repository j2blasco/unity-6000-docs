* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).GetContacts
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
## Declaration
public int GetContacts(ContactPoint2D[] contacts); 
### Parameters
Parameter | Description  
---|---  
contacts | An array of [ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `contacts` array. 
### Description
Retrieves all contact points for this Collider.
Contacts involving a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) set to be a trigger will never be returned here because trigger Colliders do not have contact points.  
  
You should pass an array that is large enough to contain all the contacts you want returned. This array would typically be reused so it should be of a size that can return a reasonable quantity of contacts. No allocations occur in this function which means no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts(Collider2D[] colliders); 
### Parameters
Parameter | Description  
---|---  
colliders | An array of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `colliders` array. 
### Description
Retrieves all colliders in contact with this Collider.
You should pass an array that is large enough to contain all the contacts you want returned. This array would typically be reused so it should be of a size that can return a reasonable quantity of contacts. No allocations occur in this function which means no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, ContactPoint2D[] contacts); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
contacts | An array of [ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `contacts` array. 
### Description
Retrieves all contact points for this Collider, with the results filtered by the `contactFilter`.
Contacts involving a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) set to be a trigger will never be returned here because trigger Colliders do not have contact points. This is true even if the `contactFilter` has its [ContactFilter2D.useTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D-useTriggers.html) set to true.  
  
You should pass an array that is large enough to contain all the contacts you want returned. This array would typically be reused so it should be of a size that can return a reasonable quantity of contacts. No allocations occur in this function which means no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, Collider2D[] colliders); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
colliders | An array of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
### Returns
**int** Returns the number of colliders placed in the `colliders` array. 
### Description
Retrieves all colliders in contact with this Collider, with the results filtered by the `contactFilter`.
You should pass an array that is large enough to contain all the contacts you want returned. This array would typically be reused so it should be of a size that can return a reasonable quantity of contacts. No allocations occur in this function which means no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts(List<ContactPoint2D> contacts); 
### Parameters
Parameter | Description  
---|---  
contacts | A list of [ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `contacts` list. 
### Description
Retrieves all contact points for this Collider.
Contacts involving a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) set to be a trigger will never be returned here because trigger Colliders do not have contact points.  
  
The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts(List<Collider2D> colliders); 
### Parameters
Parameter | Description  
---|---  
colliders | A list of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `colliders` list. 
### Description
Retrieves all colliders in contact with this Collider.
The results list will be resized if it doesn't contain enough elements to report all the results.This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<ContactPoint2D> contacts); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
contacts | A list of [ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `contacts` list. 
### Description
Retrieves all contact points for this Collider, with the results filtered by the `contactFilter`.
Contacts involving a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) set to be a trigger will never be returned here because trigger Colliders do not have contact points.  
  
The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
## Declaration
public int GetContacts([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<Collider2D> colliders); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
colliders | A list of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
### Returns
**int** Returns the number of contacts placed in the `colliders` list. 
### Description
Retrieves all colliders in contact with this Collider, with the results filtered by the `contactFilter`.
The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html) and [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html).
* * *
