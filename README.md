<h1 align="center"><b>BeAgLE_OS-v3</b></h1>


<div align="center">
  <img src="https://github.com/GFCACACE/BeAgLE_OS-v3/assets/88559192/7afb108d-b413-42aa-b25a-b0516999c334" alt="BeAgLE_OS-Logo" width=500 >
</div>
<div>
  <p>
  Emulate a virtual organization on a operative system powered by AI.
  </p>
</div>

<div>
<h2><b>Requirements</b></h2>

At first, you need to have Conda installed. Then create a new environment and install the requirements.txt:

```conda
conda create --prefix path/to/the/environment/directory
conda activate path/to/the/environment/directory
conda install --file requirements.txt
```
</div>

<div>
<h2><b>Architecture</b></h2>
  <p><b>ACLARATION:Each module will have its own Readme.md where describes it specific use case. This is a high conceptual explanation.</b></p>


  <h3><b>Persistent Storage</b></h3>
  <p>This module is where all organizations' deployment happens.</p>
  <p>Inside each organization you will have a space for creating databases where the Agents can manage all the business data, another space for create and develop services that the entity provides, where inside are many procedures like administrative circuits, controls, etc. Each one has a project folder that is going to be used by the TaskWeaver agent to plan and execute the task, where there you must include many processes/tasks (plugins) for the completion of this.</p>
  
  <img src="https://github.com/GFCACACE/BeAgLE_OS-v3/assets/88559192/9899dfe6-4b8e-444f-94fb-58c43906ff0c" align="center">

<h3><b>Controller</b></h3>
  <img src="https://github.com/GFCACACE/BeAgLE_OS-v3/assets/88559192/70d5d87d-18d5-4edd-93c2-139970073985" align="center">
  <p>This module is where the admin manage the system with a UI that is going to trigger both for events that require the agent and fixed scripts to perform a certain action.</p>
</div>

<div>
  <h3><b>Following Steps</b></h3>
  * Create each particular module with the minimum functions required for the MVP.
  * Effective communication between modules.
  * Design the UI.
</div>
<div>
  <h3><b>Contact</b></h3>
  [Connect with me on LinkedIn](https://www.linkedin.com/in/federico-cacace-137abb212/)

</div>
