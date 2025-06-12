* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-custom-serialization.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html)
  * Custom serialization


[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-rules.html)
Serialization rules
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-how-unity-uses.html)
How Unity uses serialization
# Custom serialization
When you want to serialize something that Unity’s serializer doesn’t support (for example, a C# Dictionary) you can implement the [ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html) interface in your class. This allows you to implement callbacks that Unity invokes at key points during serialization and deserialization.
You can use serialization callbacks to give your hard-to-serialize data a different representation at runtime than at serialization time. You can transform your data into something Unity understands just before Unity serializes it. After Unity has written the data to your fields, you can transform the serialized data back into the form you want it to have at runtime.
  1. When an object is about to be serialized, Unity invokes the `OnBeforeSerialize()` callback. In this callback you can transform your data into something Unity understands. For example, to serialize a C# Dictionary, copy the data from the Dictionary into an array of keys and an array of values.
  2. After the `OnBeforeSerialize()` callback is complete, Unity serializes the arrays.
  3. Later, when the object is deserialized, Unity invokes the `OnAfterDeserialize()` callback. In this callback you can transform the data back into a form that’s convenient for the object in memory. For example, use the key and value arrays to repopulate the C# Dictionary.


## Example 1: Unity’s default serialization causes performance issues
Suppose you want to have a tree data structure. If you let Unity serialize the data structure directly, the “no support for null” limitation would cause your data stream to become very big, leading to performance degradations in many systems:
```

using UnityEngine;
using System.Collections.Generic;
using System;

public class VerySlowBehaviourDoNotDoThis : MonoBehaviour {
    [Serializable]
    public class Node {
        public string interestingValue = "value";
        //The field below is what makes the serialization data become huge because
        //it introduces a 'class cycle'.
        public List<Node> children = new List<Node>();
    }
    //this gets serialized
    public Node root = new Node();
    void OnGUI() {
        Display (root);
    }
    void Display(Node node) {
        GUILayout.Label ("Value: ");
        node.interestingValue = GUILayout.TextField(node.interestingValue, GUILayout.Width(200));
        GUILayout.BeginHorizontal ();
        GUILayout.Space (20);
        GUILayout.BeginVertical ();
        foreach (var child in node.children) {
            Display (child);
        }
        if (GUILayout.Button ("Add child")) {
            node.children.Add (new Node ());
        }
        GUILayout.EndVertical ();
        GUILayout.EndHorizontal ();
    }
}

```

## Example 2: Custom serialization avoids performance issues
In this case, you tell Unity not to serialize the tree directly, and you make a separate field to store the tree in a serialized format, suited to Unity’s serializer:
```

using System.Collections.Generic;
using System;

public class BehaviourWithTree : MonoBehaviour, ISerializationCallbackReceiver {
    // Node class that is used at runtime.
    // This is internal to the BehaviourWithTree class and is not serialized.
    public class Node {
        public string interestingValue = "value";
        public List<Node> children = new List<Node>();
    }
    // Node class that we will use for serialization.
    [Serializable]
    public struct SerializableNode {
        public string interestingValue;
        public int childCount;
        public int indexOfFirstChild;
    }
    // The root node used for runtime tree representation. Not serialized.
    Node root = new Node();
    // This is the field we give Unity to serialize.
    public List<SerializableNode> serializedNodes;
    public void OnBeforeSerialize() {
        // Unity is about to read the serializedNodes field's contents.
        // The correct data must now be written into that field "just in time".
        if (serializedNodes == null) serializedNodes = new List<SerializableNode>();
        if (root == null) root = new Node ();
        serializedNodes.Clear();
        AddNodeToSerializedNodes(root);
        // Now Unity is free to serialize this field, and we should get back the expected 
        // data when it is deserialized later.
    }
    void AddNodeToSerializedNodes(Node n) {
        var serializedNode = new SerializableNode () {
            interestingValue = n.interestingValue,
            childCount = n.children.Count,
            indexOfFirstChild = serializedNodes.Count+1
        }
        ;
        serializedNodes.Add (serializedNode);
        foreach (var child in n.children) {
            AddNodeToSerializedNodes (child);
        }
    }
    public void OnAfterDeserialize() {
        //Unity has just written new data into the serializedNodes field.
        //let's populate our actual runtime data with those new values.
        if (serializedNodes.Count > 0) {
            ReadNodeFromSerializedNodes (0, out root);
        } else
        root = new Node ();
    }
    int ReadNodeFromSerializedNodes(int index, out Node node) {
        var serializedNode = serializedNodes [index];
        // Transfer the deserialized data into the internal Node class
        Node newNode = new Node() {
            interestingValue = serializedNode.interestingValue,
            children = new List<Node> ()
        }
        ;
        // The tree needs to be read in depth-first, since that's how we wrote it out.
        for (int i = 0; i != serializedNode.childCount; i++) {
            Node childNode;
            index = ReadNodeFromSerializedNodes (++index, out childNode);
            newNode.children.Add (childNode);
        }
        node = newNode;
        return index;
    }
    // This OnGUI draws out the node tree in the Game View, with buttons to add new nodes as children.
    void OnGUI() {
        if (root != null) {
            Display (root);
        }
    }
    void Display(Node node) {
        GUILayout.Label ("Value: ");
        // Allow modification of the node's "interesting value".
        node.interestingValue = GUILayout.TextField(node.interestingValue, GUILayout.Width(200));
        GUILayout.BeginHorizontal ();
        GUILayout.Space (20);
        GUILayout.BeginVertical ();
        foreach (var child in node.children) {
            Display (child);
        }
        if (GUILayout.Button ("Add child")) {
            node.children.Add (new Node ());
        }
        GUILayout.EndVertical ();
        GUILayout.EndHorizontal ();
    }
}


```

  
  

## Additional resources
  * [Serialization rules](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-rules.html)
  * [How Unity uses serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-how-unity-uses.html)
  * [JSONSerialization](https://docs.unity3d.com/6000.0/Documentation/Manual/json-serialization.html)
  * [Serialization best practices](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-best-practices.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-rules.html)
Serialization rules
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-how-unity-uses.html)
How Unity uses serialization
