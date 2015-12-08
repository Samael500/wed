ip_address = "10.1.1.111"
hostname = "mywed"

Vagrant.configure(2) do |config|
  # Virtual machine parameters
  config.vm.box = "bento/debian-8.1"
  # config.vm.box = "Samael500/#{hostname}"
  config.vm.network "private_network", ip: ip_address
  config.vm.synced_folder ".", "/home/vagrant/proj", type: "nfs", :mount_options => ['actimeo=2']
  config.vm.hostname = hostname
  config.vm.post_up_message = "#{hostname} dev server successfuly started.
    Connect to host with:
    http://#{ip_address}/
    or over ssh with `vagrant ssh`

    Admin user credentials:
    login: root
    password: 123123
    "
  # Set box name
  config.vm.define :"#{hostname}_vagrant" do |t|
  end
  # Virtualbox specific parameters
  config.vm.provider "virtualbox" do |v|
    v.name = "#{hostname}_vagrant"
    v.memory = 2048
    v.cpus = 2
  end
  # Provisioning with Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/playbook.dev.yml"
  end
end
