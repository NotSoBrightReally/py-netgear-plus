<div class="box_css">
<div id="module_div"class='module-div'>
<div class='module-title' style='padding-left: 0px;'>ml343</div>
<div class='module-content'>
<div class='module-content-text'>ml346</div>
</div>
<div class='module-content'>
<div class="module-content-header">ml334</div>
<div class='module-content-text'>ml335</div>
<div class='clearfix'>
<div class='checkbox'><input id='uninterruptedPoeStatus' type='checkbox' onclick="toggleSelect();submitUninterruptedPoE();" checked><label></label></div>
</div>
</div>
<div class='module-content'>
<div class="module-content-header">ml338</div>
<div class='module-content-text'>ml342</div>
</div>
<div class='port_list_content' style='margin-top:-10px;'>
<ul class="cable_test_port_list">
<li class="port_circle"><span class="port_circle_num">1</span></li>
<li class="port_circle"><span class="port_circle_num">2</span></li>
<li class="port_circle"><span class="port_circle_num">3</span></li>
<li class="port_circle"><span class="port_circle_num">4</span></li>
<li class="port_circle"><span class="port_circle_num">5</span></li>
<li class="port_circle"><span class="port_circle_num">6</span></li>
<li class="port_circle"><span class="port_circle_num">7</span></li>
<li class="port_circle"><span class="port_circle_num">8</span></li>
</ul>
</div>
<div class='submit_btn cabletestBtn' style='margin-top:0;margin-bottom:0;'>
<span class='text-primary'>
<button name='submitPwrCyclePorts' data-react-toolbox='button' onclick="submitPwrCyclePorts();" class='toolbox_lib_button button_theme_flat button_theme_primary button_theme_mini button button_mini' disabled=''>APPLY</button>
</span>
<span class='text-muted'>
<button name='cancelPwrCyclePorts' data-react-toolbox='button' onclick="cancelCableTest();disableButtons();" class='toolbox_lib_button button_theme_flat button_theme_default button_theme_mini button button_mini' disabled=''>CANCEL</button>
</span>
</div>
</div>
<div style="margin-top:-10px;">
<div class="poe-port-box" id="poe_port_list"  style="position:relative">
<div class="widget_header">
<div class="widget_header_title">
<ul class="poe_port_list">
<li class="active" id="poeSettingSelect" onclick="changePoeEditOption(this)">
<p style='font-size:0.875rem;'>ml595</p></li>
<li id="poeStatusSelect" onclick="changePoeEditOption(this)">
<p style='font-size:0.875rem;'>ml583</p></li>
<div class="indicator"></div>
</ul>
</div>
</div>
<div class="box_flex" id="poe_port_list_show">
<div style='color:#817d88;height:3.125rem;border-bottom: 1px solid rgba(46, 43, 51, .5);'>
<ul class="poe_port_list" style="padding-left:1.875rem;">
<li><p style="text-align:left">ml578</p></li>
<li><p style="text-align:left">ml549</p></li>
<li><p style="text-align:left">ml553</p></li>
</ul>
</div>
<div id="poe_port_details" class="box_flex">
<ul class="list_css">
<li class="poe_port_list_item poePortSettingListItem index_li">
<div name='isShowPot1' class="poe_li_header_content">
<i class="mid_title_icon icon_color_gray icon_sm accordion_icon accordion_plus pull-right" style="padding-right:12%;">
<span class="icon-expand"></span>
</i>
<span class="pull-right poe-power-mode">
<span>802.3at</span>
<input type="hidden" class="pwrMode" id="hidPwrMode" value="3"></span>
<span class="pull-right poe-portPwr-width">
<span class="portPwr">Enable</span>
<input type="hidden" class="hidPortPwr" id="hidPortPwr" value="1">
</span>
<span class="poe_index_li_title poe-port-index">
<input type="hidden" class="port" value="1">
<span style='text-overflow:ellipsis;overflow:hidden;white-space:nowrap;width:100%;display:inline-block;'>1 - wax610b </span></span></div>
<input type="hidden" class="portName" value="wax610b">
<div class="poe_port_info">
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml551</span>
</div>
<div>
<span class="portPrioShow">Low</span>
<input type="hidden" class="portPrio" id="hidPortPrio" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml554</span>
</div>
<div>
<span class="pwrLimTypeShow">User</span>
<input type="hidden" class="pwrLimitType" id="hidLimitType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml557</span>
</div>
<div>
<span class="pwrLimitShow">30.0</span>
<input type="hidden" class="pwrLimit" value="30.0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml559</span>
</div>
<div>
<span class="detecTypeShow">IEEE 802</span>
<input type="hidden" class="detecType" id="hidDetecType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml975</span>
</div>
<div>
<span class="longerDetectShow">Disable</span>
<input type="hidden" class="longerDetect" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-12">
<div onclick="edit_poe_port_info();" class="poe_edit_btn">
<button name='editPot1' data-react-toolbox="button" class="toolbox_lib_button button_theme_flat button_theme_primary button_theme_mini button button_mini">
EDIT
</button>
</div>
</div>
</div>
</li>
<li class="poe_port_list_item poePortSettingListItem index_li">
<div name='isShowPot2' class="poe_li_header_content">
<i class="mid_title_icon icon_color_gray icon_sm accordion_icon accordion_plus pull-right" style="padding-right:12%;">
<span class="icon-expand"></span>
</i>
<span class="pull-right poe-power-mode">
<span>802.3at</span>
<input type="hidden" class="pwrMode" id="hidPwrMode" value="3"></span>
<span class="pull-right poe-portPwr-width">
<span class="portPwr">Enable</span>
<input type="hidden" class="hidPortPwr" id="hidPortPwr" value="1">
</span>
<span class="poe_index_li_title poe-port-index">
<input type="hidden" class="port" value="2">
<span style='text-overflow:ellipsis;overflow:hidden;white-space:nowrap;width:100%;display:inline-block;'>2 - wax610a </span></span></div>
<input type="hidden" class="portName" value="wax610a">
<div class="poe_port_info">
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml551</span>
</div>
<div>
<span class="portPrioShow">Low</span>
<input type="hidden" class="portPrio" id="hidPortPrio" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml554</span>
</div>
<div>
<span class="pwrLimTypeShow">User</span>
<input type="hidden" class="pwrLimitType" id="hidLimitType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml557</span>
</div>
<div>
<span class="pwrLimitShow">30.0</span>
<input type="hidden" class="pwrLimit" value="30.0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml559</span>
</div>
<div>
<span class="detecTypeShow">IEEE 802</span>
<input type="hidden" class="detecType" id="hidDetecType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml975</span>
</div>
<div>
<span class="longerDetectShow">Disable</span>
<input type="hidden" class="longerDetect" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-12">
<div onclick="edit_poe_port_info();" class="poe_edit_btn">
<button name='editPot2' data-react-toolbox="button" class="toolbox_lib_button button_theme_flat button_theme_primary button_theme_mini button button_mini">
EDIT
</button>
</div>
</div>
</div>
</li>
<li class="poe_port_list_item poePortSettingListItem index_li">
<div name='isShowPot3' class="poe_li_header_content">
<i class="mid_title_icon icon_color_gray icon_sm accordion_icon accordion_plus pull-right" style="padding-right:12%;">
<span class="icon-expand"></span>
</i>
<span class="pull-right poe-power-mode">
<span>802.3at</span>
<input type="hidden" class="pwrMode" id="hidPwrMode" value="3"></span>
<span class="pull-right poe-portPwr-width">
<span class="portPwr">Enable</span>
<input type="hidden" class="hidPortPwr" id="hidPortPwr" value="1">
</span>
<span class="poe_index_li_title poe-port-index">
<input type="hidden" class="port" value="3">
<span style='text-overflow:ellipsis;overflow:hidden;white-space:nowrap;width:100%;display:inline-block;'>3 - loki </span></span></div>
<input type="hidden" class="portName" value="loki">
<div class="poe_port_info">
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml551</span>
</div>
<div>
<span class="portPrioShow">Low</span>
<input type="hidden" class="portPrio" id="hidPortPrio" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml554</span>
</div>
<div>
<span class="pwrLimTypeShow">User</span>
<input type="hidden" class="pwrLimitType" id="hidLimitType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml557</span>
</div>
<div>
<span class="pwrLimitShow">30.0</span>
<input type="hidden" class="pwrLimit" value="30.0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml559</span>
</div>
<div>
<span class="detecTypeShow">IEEE 802</span>
<input type="hidden" class="detecType" id="hidDetecType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml975</span>
</div>
<div>
<span class="longerDetectShow">Disable</span>
<input type="hidden" class="longerDetect" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-12">
<div onclick="edit_poe_port_info();" class="poe_edit_btn">
<button name='editPot3' data-react-toolbox="button" class="toolbox_lib_button button_theme_flat button_theme_primary button_theme_mini button button_mini">
EDIT
</button>
</div>
</div>
</div>
</li>
<li class="poe_port_list_item poePortSettingListItem index_li">
<div name='isShowPot4' class="poe_li_header_content">
<i class="mid_title_icon icon_color_gray icon_sm accordion_icon accordion_plus pull-right" style="padding-right:12%;">
<span class="icon-expand"></span>
</i>
<span class="pull-right poe-power-mode">
<span>802.3at</span>
<input type="hidden" class="pwrMode" id="hidPwrMode" value="3"></span>
<span class="pull-right poe-portPwr-width">
<span class="portPwr">Enable</span>
<input type="hidden" class="hidPortPwr" id="hidPortPwr" value="1">
</span>
<span class="poe_index_li_title poe-port-index">
<input type="hidden" class="port" value="4">
<span style='text-overflow:ellipsis;overflow:hidden;white-space:nowrap;width:100%;display:inline-block;'>4 - homeassistant </span></span></div>
<input type="hidden" class="portName" value="homeassistant">
<div class="poe_port_info">
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml551</span>
</div>
<div>
<span class="portPrioShow">Low</span>
<input type="hidden" class="portPrio" id="hidPortPrio" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml554</span>
</div>
<div>
<span class="pwrLimTypeShow">User</span>
<input type="hidden" class="pwrLimitType" id="hidLimitType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml557</span>
</div>
<div>
<span class="pwrLimitShow">30.0</span>
<input type="hidden" class="pwrLimit" value="30.0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml559</span>
</div>
<div>
<span class="detecTypeShow">IEEE 802</span>
<input type="hidden" class="detecType" id="hidDetecType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml975</span>
</div>
<div>
<span class="longerDetectShow">Disable</span>
<input type="hidden" class="longerDetect" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-12">
<div onclick="edit_poe_port_info();" class="poe_edit_btn">
<button name='editPot4' data-react-toolbox="button" class="toolbox_lib_button button_theme_flat button_theme_primary button_theme_mini button button_mini">
EDIT
</button>
</div>
</div>
</div>
</li>
<li class="poe_port_list_item poePortSettingListItem index_li">
<div name='isShowPot5' class="poe_li_header_content">
<i class="mid_title_icon icon_color_gray icon_sm accordion_icon accordion_plus pull-right" style="padding-right:12%;">
<span class="icon-expand"></span>
</i>
<span class="pull-right poe-power-mode">
<span>802.3at</span>
<input type="hidden" class="pwrMode" id="hidPwrMode" value="3"></span>
<span class="pull-right poe-portPwr-width">
<span class="portPwr">Enable</span>
<input type="hidden" class="hidPortPwr" id="hidPortPwr" value="1">
</span>
<span class="poe_index_li_title poe-port-index">
<input type="hidden" class="port" value="5">
<span>5</span></span></div>
<input type="hidden" class="portName" value="">
<div class="poe_port_info">
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml551</span>
</div>
<div>
<span class="portPrioShow">Low</span>
<input type="hidden" class="portPrio" id="hidPortPrio" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml554</span>
</div>
<div>
<span class="pwrLimTypeShow">User</span>
<input type="hidden" class="pwrLimitType" id="hidLimitType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml557</span>
</div>
<div>
<span class="pwrLimitShow">30.0</span>
<input type="hidden" class="pwrLimit" value="30.0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml559</span>
</div>
<div>
<span class="detecTypeShow">IEEE 802</span>
<input type="hidden" class="detecType" id="hidDetecType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml975</span>
</div>
<div>
<span class="longerDetectShow">Disable</span>
<input type="hidden" class="longerDetect" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-12">
<div onclick="edit_poe_port_info();" class="poe_edit_btn">
<button name='editPot5' data-react-toolbox="button" class="toolbox_lib_button button_theme_flat button_theme_primary button_theme_mini button button_mini">
EDIT
</button>
</div>
</div>
</div>
</li>
<li class="poe_port_list_item poePortSettingListItem index_li">
<div name='isShowPot6' class="poe_li_header_content">
<i class="mid_title_icon icon_color_gray icon_sm accordion_icon accordion_plus pull-right" style="padding-right:12%;">
<span class="icon-expand"></span>
</i>
<span class="pull-right poe-power-mode">
<span>802.3at</span>
<input type="hidden" class="pwrMode" id="hidPwrMode" value="3"></span>
<span class="pull-right poe-portPwr-width">
<span class="portPwr">Enable</span>
<input type="hidden" class="hidPortPwr" id="hidPortPwr" value="1">
</span>
<span class="poe_index_li_title poe-port-index">
<input type="hidden" class="port" value="6">
<span>6</span></span></div>
<input type="hidden" class="portName" value="">
<div class="poe_port_info">
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml551</span>
</div>
<div>
<span class="portPrioShow">Low</span>
<input type="hidden" class="portPrio" id="hidPortPrio" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml554</span>
</div>
<div>
<span class="pwrLimTypeShow">User</span>
<input type="hidden" class="pwrLimitType" id="hidLimitType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml557</span>
</div>
<div>
<span class="pwrLimitShow">30.0</span>
<input type="hidden" class="pwrLimit" value="30.0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml559</span>
</div>
<div>
<span class="detecTypeShow">IEEE 802</span>
<input type="hidden" class="detecType" id="hidDetecType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml975</span>
</div>
<div>
<span class="longerDetectShow">Disable</span>
<input type="hidden" class="longerDetect" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-12">
<div onclick="edit_poe_port_info();" class="poe_edit_btn">
<button name='editPot6' data-react-toolbox="button" class="toolbox_lib_button button_theme_flat button_theme_primary button_theme_mini button button_mini">
EDIT
</button>
</div>
</div>
</div>
</li>
<li class="poe_port_list_item poePortSettingListItem index_li">
<div name='isShowPot7' class="poe_li_header_content">
<i class="mid_title_icon icon_color_gray icon_sm accordion_icon accordion_plus pull-right" style="padding-right:12%;">
<span class="icon-expand"></span>
</i>
<span class="pull-right poe-power-mode">
<span>802.3af</span>
<input type="hidden" class="pwrMode" id="hidPwrMode" value="0"></span>
<span class="pull-right poe-portPwr-width">
<span class="portPwr">Disable</span>
<input type="hidden" class="hidPortPwr" id="hidPortPwr" value="0">
</span>
<span class="poe_index_li_title poe-port-index">
<input type="hidden" class="port" value="7">
<span>7</span></span></div>
<input type="hidden" class="portName" value="">
<div class="poe_port_info">
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml551</span>
</div>
<div>
<span class="portPrioShow">Low</span>
<input type="hidden" class="portPrio" id="hidPortPrio" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml554</span>
</div>
<div>
<span class="pwrLimTypeShow">None</span>
<input type="hidden" class="pwrLimitType" id="hidLimitType" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml557</span>
</div>
<div>
<span class="pwrLimitShow">16.2</span>
<input type="hidden" class="pwrLimit" value="16.2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml559</span>
</div>
<div>
<span class="detecTypeShow"></span>
<input type="hidden" class="detecType" id="hidDetecType" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml975</span>
</div>
<div>
<span class="longerDetectShow">Get Value Fault</span>
<input type="hidden" class="longerDetect" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-12">
<div onclick="edit_poe_port_info();" class="poe_edit_btn">
<button name='editPot7' data-react-toolbox="button" class="toolbox_lib_button button_theme_flat button_theme_primary button_theme_mini button button_mini">
EDIT
</button>
</div>
</div>
</div>
</li>
<li class="poe_port_list_item poePortSettingListItem index_li">
<div name='isShowPot8' class="poe_li_header_content">
<i class="mid_title_icon icon_color_gray icon_sm accordion_icon accordion_plus pull-right" style="padding-right:12%;">
<span class="icon-expand"></span>
</i>
<span class="pull-right poe-power-mode">
<span>802.3at</span>
<input type="hidden" class="pwrMode" id="hidPwrMode" value="3"></span>
<span class="pull-right poe-portPwr-width">
<span class="portPwr">Disable</span>
<input type="hidden" class="hidPortPwr" id="hidPortPwr" value="0">
</span>
<span class="poe_index_li_title poe-port-index">
<input type="hidden" class="port" value="8">
<span style='text-overflow:ellipsis;overflow:hidden;white-space:nowrap;width:100%;display:inline-block;'>8 - upstream </span></span></div>
<input type="hidden" class="portName" value="upstream">
<div class="poe_port_info">
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml551</span>
</div>
<div>
<span class="portPrioShow">Low</span>
<input type="hidden" class="portPrio" id="hidPortPrio" value="0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml554</span>
</div>
<div>
<span class="pwrLimTypeShow">User</span>
<input type="hidden" class="pwrLimitType" id="hidLimitType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml557</span>
</div>
<div>
<span class="pwrLimitShow">30.0</span>
<input type="hidden" class="pwrLimit" value="30.0">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml559</span>
</div>
<div>
<span class="detecTypeShow">IEEE 802</span>
<input type="hidden" class="detecType" id="hidDetecType" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-6">
<div class="hid_info_title">
<span class='hid-txt wid-full'>ml975</span>
</div>
<div>
<span class="longerDetectShow">Disable</span>
<input type="hidden" class="longerDetect" value="2">
</div>
</div>
<div class="hid_info_cell col-xs-12 col-sm-12">
<div onclick="edit_poe_port_info();" class="poe_edit_btn">
<button name='editPot8' data-react-toolbox="button" class="toolbox_lib_button button_theme_flat button_theme_primary button_theme_mini button button_mini">
EDIT
</button>
</div>
</div>
</div>
</li>
</ul></div></div>
<div class="poe_box_css volumes-scss widget_height has-bottom-opacity-effect " id="poe_port_edit">
</div>
<div class="box_flex" id="poe_port_status_show"></div>
</div>
</div>
</div>
<input type=hidden name='hash' id='hash' value="3483299a0487987b90483a70c5d3d2dd">
<script type="text/javascript">
function toggleSelectPort()
{
var $port = $(".cable_test_port_list li");
$port.click(function(){
$(this).toggleClass("port_circle_selected");
if($port.hasClass("port_circle_selected")==false){
 disableButtons();
}
else{
 enableButtons();
}
});
}
$(document).ready(function(){
    toggleSelectPort();
    collapseOrExpandPoeBlock($(".poePortSettingListItem .poe_li_header_content"), $(".poe_port_info"), $(".poePortSettingListItem .poe_li_header_content .mid_title_icon span"));
    edit_poe_port_info();
    back_poe_port_info();
    transPage($('#transContent')[0]);
});
</script>
