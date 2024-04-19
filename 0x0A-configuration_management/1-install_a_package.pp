#Using Puppet, install flask from pip3
package { 'werkzeug.url':
  ensure =>'installed',
}

package { 'flask':
  ensure   =>'2.1.0',
  provider =>'pip3',
  before  =>'werkzeug',
}

