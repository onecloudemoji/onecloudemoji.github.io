from flask import Flask
from pyVim import connect
from pyVmomi import vim
import html
import re

# details for your ESX host:
host = "192.168.14.251"
user = "root"
password = "nice_try_fucko"
port = 443

# name of (this) machine to be excluded
control_vm = "vulnlab"

def main():

    # ignore invalid cert on ESX box
    import ssl
    _create_unverified_https_context = ssl._create_unverified_context
    ssl._create_default_https_context = _create_unverified_https_context

    vm_list_l1 = get_vm_list_l1()
    vm_list_l2 = get_vm_list_l2()

    app = Flask(__name__)

    @app.route("/")
    def index():
        result = '''<!DOCTYPE html>
<html>
  <head>
    <title>Revert Panel</title>
  </head>
  <body>
    <h1>Level 1</h1>
<form onsubmit="return redirectTo(this)">
<select name = "1" value="GO">
'''
        for name, uuid in sorted(vm_list_l1.items()):
            name_mod = name.replace("_l1","")
            result += '    <option value="/reset1/' + name + '">' + name_mod + '</option>\n'

        result += '''  

</select>
 <input type="submit" value="Revert">
</form>

<script>
  function redirectTo(elem) {
    event.preventDefault();
    top.location.href = elem.firstElementChild.options[elem.firstElementChild.selectedIndex].value
  }
</script>

<div id="l2">
<br>
    <h1>Level 2</h1>
<form onsubmit="return redirectTo(this)">
<select name = "2" value="GO">
'''
        for name, uuid in sorted(vm_list_l2.items()):
            name_mod = name.replace("_l2","") 
 
            result += '    <option value="/reset2/' + name + '">' + name_mod + '</option>\n'

        result += '''  

</select>
 <input type="submit" value="Revert">
</form>


</div>

<div id="l3">
<br>
    <h1>Level 3</h1>
<form onsubmit="return redirectTo(this)">
<select name = "3" value="GO">
'''
        for name, uuid in sorted(vm_list_l2.items()):
            name_mod = name.replace("_l3","") 
 
            result += '    <option value="/reset3/' + name + '">' + name_mod + '</option>\n'

        result += '''  

</select>
 <input type="submit" value="Revert">
</form>


</div>


<div id="l4">
<br>
    <h1>Level 4</h1>
<form onsubmit="return redirectTo(this)">
<select name = "4" value="GO">
'''
        for name, uuid in sorted(vm_list_l2.items()):
            name_mod = name.replace("_l4","") 
 
            result += '    <option value="/reset3/' + name + '">' + name_mod + '</option>\n'

        result += '''  

</select>
 <input type="submit" value="Revert">
</form>


</div>
<div id="password">
<form onsubmit="checkform()">
 <label for="password">Enter password to unlock additional levels:</label><br>
<input type="text" id="secret" name="password">
<input type="submit" value="Submit"> 
</form>
<script>
</div>


var x = document.getElementById("l2");
if (document.cookie.match(/^(.*;)?\s*MyCookie\s*=\s*[^;]+(.*)?$/)) 
	{
    x.style.display = "inline";
	} 
else 
    {
    x.style.display = "none";
    }


	
</script>



<script>



var x = document.getElementById("l3");
if (document.cookie.match(/^(.*;)?\s*MyCookiel3\s*=\s*[^;]+(.*)?$/)) 
	{
    x.style.display = "inline";
	} 
else 
    {
    x.style.display = "none";
    }


	
</script>

<script>



var x = document.getElementById("l4");
var y = document.getElementById("password");
if (document.cookie.match(/^(.*;)?\s*MyCookiel4\s*=\s*[^;]+(.*)?$/)) 
	{
    x.style.display = "inline";
    y.style.display = "none";
	} 
else 
    {
    x.style.display = "none";
	y.style.display = "inline";
    }


	
</script>



<script>
function checkform(){
    
    var form1 = document.getElementById('secret');
    if(secret.value == "TEST")
    {
        
		alert("FOUND TEST LEVEL");
		document.cookie = "MyCookie=MyCookie"; 
            
		
    }   
}
</script>


<script>
function checkform(){
    
    var form1 = document.getElementById('secret');
    if(secret.value == "TEST")
    {
        
		alert("FOUND TEST LEVEL");
		document.cookie = "MyCookie=MyCookie"; 
            
		
    }   
}
</script><script>
function checkform(){
    
    var form1 = document.getElementById('secret');
    if(secret.value == "TEST2")
    {
        
		alert("FOUND L3 LEVEL");
		document.cookie = "MyCookiel3=MyCookiel3"; 
            
		
    }   
}
</script>


<script>
function checkform(){
    
    var form1 = document.getElementById('secret');
    if(secret.value == "TEST3")
    {
        
		alert("FOUND FINAL LEVEL");
		document.cookie = "MyCookiel4=MyCookiel4"; 
            
		
    }   
}
</script>



</body>
</html>
'''
        return result, 200

    @app.route("/reset1/<string:vm_name>")
    def reset(vm_name):
        reset_vm_l1(vm_list_l1, vm_name)
        return 'OK\n', 200
		
    @app.route("/reset2/<string:vm_name>")
    def reset2(vm_name):
        reset_vm_l2(vm_list_l2, vm_name)
        return 'OK\n', 200		

    # start the web server
    app.run(host="127.0.0.2", port=80)

def get_vm_list_l1():

    # make connection
    service_instance = connect.SmartConnect(host=host, user=user, pwd=password, port=int(port))

    # create list of machines
    content = service_instance.RetrieveContent()
    containerView = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    children = containerView.view
    vm_list_l1 = {}
	
    for child in children:
        summary = child.summary
        if not summary.config.name == control_vm:
            if "_l1" in summary.config.name:		
                vm_list_l1[summary.config.name] = summary.config.uuid
                
            

    connect.Disconnect(service_instance)
    
    return vm_list_l1

def get_vm_list_l2():

    # make connection
    service_instance = connect.SmartConnect(host=host, user=user, pwd=password, port=int(port))

    # create list of machines
    content = service_instance.RetrieveContent()
    containerView = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    children = containerView.view
    vm_list_l2 = {}
	
    for child in children:
        summary = child.summary
        if not summary.config.name == control_vm:
            if "_l2" in summary.config.name:
                vm_list_l2[summary.config.name] = summary.config.uuid
                
             

    connect.Disconnect(service_instance)
    
    return vm_list_l2
	

def reset_vm_l1(vm_list_l1, target_name):

    # make sure target is in list
    target_uuid = vm_list_l1[target_name]

    if target_uuid:
        # make connection
        service_instance = connect.SmartConnect(host=host, user=user, pwd=password, port=int(port))
        target_vm = service_instance.content.searchIndex.FindByUuid(None, target_uuid, True)

        if target_vm:
#            print(target_vm.runtime.powerState)
            target_vm.ResetVM_Task()

        connect.Disconnect(service_instance)
		

def reset_vm_l2(vm_list_l2, target_name):

    # make sure target is in list
    target_uuid = vm_list_l2[target_name]

    if target_uuid:
        # make connection
        service_instance = connect.SmartConnect(host=host, user=user, pwd=password, port=int(port))
        target_vm = service_instance.content.searchIndex.FindByUuid(None, target_uuid, True)

        if target_vm:
#            print(target_vm.runtime.powerState)
            target_vm.ResetVM_Task()

        connect.Disconnect(service_instance)


if __name__ == "__main__":
    main()
