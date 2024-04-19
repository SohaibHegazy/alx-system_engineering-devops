#Using Puppet, install flask from pip3
package { 'werkzeug':
  ensure   =>'installed',
  provider =>'pypi',
}

package { 'flask':
  ensure   =>'2.1.0',
  provider =>'pip3',
  require  =>'werkzeug',
}

