#Using Puppet, install flask from pip3
package { 'flask':
  ensure   =>'installed',
  provider =>'pip3',
  ensure   =>'2.1.0',
}

