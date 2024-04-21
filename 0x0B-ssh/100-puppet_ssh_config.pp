#!/usr/bin/env bash
# set up client SSH configuration file to connect to server without password
file_line { 'Identity':
           ensure => 'present',
           path   => '/etc/ssh/ssh_config',
           line   => '  IdentityFile ~/.ssh/school',
           }

file_line { 'Refuse password':
           path   => '/etc/ssh/ssh_config',
           line   => '  PasswordAuthentication no',
           }
