# Using Puppet, install flask from pip3
package { 'werkzeug':
  ensure   =>'installed',
}

package { 'flask':
  ensure   =>'2.1.0',
  name     =>'flask',
  provider =>'pip3',
  require  =>Package['werkzeug'],
}

