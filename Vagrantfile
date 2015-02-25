Vagrant.configure(2) do |config|
  # Virtual machine parameters
  config.vm.box = "chef/debian-7.6"
  config.vm.network "private_network", ip: "10.1.1.111"
  config.vm.synced_folder ".", "/home/vagrant/proj"
  config.vm.hostname = "mywed"
  config.vm.post_up_message = "mywed dev server successfuly started.
    Connect to host with:
    http://10.1.1.111/
    or over ssh with `vagrant ssh`

    Admin user credentials:
    login: root
    password: 123123
    "
  # Set box name
  config.vm.define :mywed_vagrant do |t|
  end
  # Virtualbox specific parameters
  config.vm.provider "virtualbox" do |v|
    v.name = "mywed_vagrant"
    v.memory = 1024
    v.cpus = 1
  end
  # Provisioning with Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/playbook.dev.yml"
  end
end
