from django.conf.urls import patterns, url,include
from django.contrib.auth.decorators import login_required
from schoolnew.views import *
# from django.conf.urls import patterns, include, url
# from django.views.generic import TemplateView
# from django.contrib import admin
# from django.views.generic import View
# from django.views.generic.edit import CreateView,UpdateView,DeleteView
# from schoolnew.views import *
# from django.views.decorators.cache import never_cache

# admin.autodiscover()

urlpatterns = patterns('',

    url(
        regex=r'^school_registration/$',
        view=home_page.as_view(),
        name='school_registration'
    ),

    url(
        regex=r'^office_registration/$',
        view=Off_home_page.as_view(),
        name='office_registration'
    ),
    url(
        regex=r'^office_basic_info/$',
        view=Office_basic_info.as_view(),
        name='office_basic_info'
    ),

    url(
        regex=r'^offnonteaching_edit/$',
        view=Offnonteaching_edit.as_view(),
        name='offnonteaching_edit'
    ),
    url( 
        regex=r'^offnonteaching_update/(?P<pk>\d+?)/$',
        view=Offntpost_update.as_view(),
        name='offnonteaching_update'
    ),

    url(
        regex=r'^offnonteaching_delete/(?P<pk>\d+?)/$',
        view=Offnonteaching_delete.as_view(),
        name='offnonteaching_delete'
    ),

    url(
        regex=r'^basic_info_edit/$',
        view=basic_edit.as_view(),
        name='basic_info_edit'
    ),

    url(
        regex=r'^admin_edit/$',
        view=admin_edit.as_view(),
        name='admin_edit'
    ),

    url(
        regex=r'^infra_entry/$',
        view=infra_edit.as_view(),
        name='infra_entry'
    ),
    url(
        regex=r'^infra_edit/$',
        view=infra_edit.as_view(),
        name='infra_edit'
    ),


    url(
        regex=r'^class_section_edit/$',
        view=class_section_edit.as_view(),
        name='class_section_edit'
    ),

    url(
        regex=r'^teaching_edit/$',
        view=Teaching_edit.as_view(),
        name='teaching_edit'
    ),

    url(
        regex=r'^teaching_update/(?P<pk>\d+?)/$',
        view=Teaching_update.as_view(),
        name='teaching_update'
    ),


    url(
        regex=r'^teaching_delete/(?P<pk>\d+?)/$',
        view=Teaching_delete.as_view(),
        name='teaching_delete'
    ),


    url(
        regex=r'^nonteaching_edit/$',
        view=Nonteaching_edit.as_view(),
        name='nonteaching_edit'
    ),

    url(
        regex=r'^nonteaching_update/(?P<pk>\d+?)/$',
        view=Nonteaching_update.as_view(),
        name='nonteaching_update'
    ),

    url(
        regex=r'^nonteaching_delete/(?P<pk>\d+?)/$',
        view=Nonteaching_delete.as_view(),
        name='nonteaching_delete'
    ),

    url(
        regex=r'^parttime_edit/$',
        view=Parttime_edit.as_view(),
        name='parttime_edit'
    ),


    url(
        regex=r'^parttime_update/(?P<pk>\d+?)/$',
        view=Parttime_update.as_view(),
        name='parttime_update'
    ),


    url(
        regex=r'^parttime_delete/(?P<pk>\d+?)/$',
        view=Parttime_delete.as_view(),
        name='parttime_delete'
    ),

    
    url(
        regex=r'^group_edit/$',
        view=Group_edit.as_view(),
        name='group_edit'
    ),

    url(
        regex=r'^group_update/(?P<pk>\d+?)/$',
        view=Group_update.as_view(),
        name='group_update'
    ),

    url(
        regex=r'^group_delete/(?P<pk>\d+?)/$',
        view=Group_delete.as_view(),
        name='group_delete'
    ),

    url(
        regex=r'^buildabs_edit/$',
        view=Buildabs_edit.as_view(),
        name='buildabs_edit'
    ),


    url(
        regex=r'^buildabs_update/(?P<pk>\d+?)/$',
        view=Buildabs_update.as_view(),
        name='buildabs_update'
    ),

    url(
        regex=r'^buildabs_delete/(?P<pk>\d+?)/$',
        view=Buildabs_delete.as_view(),
        name='buildabs_delete'
    ),


    url(
        regex=r'^land_edit/$',
        view=Land_edit.as_view(),
        name='land_edit'
    ),


    url(
        regex=r'^land_update/(?P<pk>\d+?)/$',
        view=Land_update.as_view(),
        name='land_update'
    ),

    url(
        regex=r'^land_delete/(?P<pk>\d+?)/$',
        view=Land_delete.as_view(),
        name='land_delete'
    ),

    url(
        regex=r'^build_edit/$',
        view=Build_edit.as_view(),
        name='build_edit'
    ),

    url(
        regex=r'^build_update/(?P<pk>\d+?)/$',
        view=Build_update.as_view(),
        name='build_update'
    ),

    url(
        regex=r'^build_delete/(?P<pk>\d+?)/$',
        view=Build_delete.as_view(),
        name='build_delete'
    ),



    url(
        regex=r'^buildabs_edit/$',
        view=Buildabs_edit.as_view(),
        name='buildabs_edit'
    ),

    url(
        regex=r'^buildabs_delete/(?P<pk>\d+?)/$',
        view=Buildabs_delete.as_view(),
        name='buildabs_delete'
    ),

    url(
        regex=r'^sports_edit/$',
        view=Sports_edit.as_view(),
        name='sports_edit'
    ),

    url(
        regex=r'^sports_update/(?P<pk>\d+?)/$',
        view=Sports_update.as_view(),
        name='sports_update'
    ),

    url(
        regex=r'^sports_delete/(?P<pk>\d+?)/$',
        view=Sports_delete.as_view(),
        name='sports_delete'
    ),


    url(
        regex=r'^ict_edit/$',
        view=Ict_edit.as_view(),
        name='ict_edit'
    ),


    url(
        regex=r'^ict_update/(?P<pk>\d+?)/$',
        view=Ict_update.as_view(),
        name='ict_update'
    ),

    url(
        regex=r'^ict_delete/(?P<pk>\d+?)/$',
        view=Ict_delete.as_view(),
        name='ict_delete'
    ),
    
    url(
        regex=r'^pass_edit/$',
        view=Passpercent_edit.as_view(),
        name='passpercent_edit'
    ),
    url(
        regex=r'^pass_update/(?P<pk>\d+?)/$',
        view=Passpercent_update.as_view(),
        name='ict_update'
    ),

    url(
        regex=r'^pass_delete/(?P<pk>\d+?)/$',
        view=Passpercent_delete.as_view(),
        name='ict_delete'
    ),
    
    url(
        regex=r'^printpdf/(?P<pk>\d+?)/$',
        view=myview1.as_view(),
        name='printpdf'
    ),

    url(
        regex=r'^sch_state_abs/$',
        view=Sch_State_abs.as_view(),
        name='sch_state_abs'
    ),  

    url(
        regex=r'^sch_dist_abs/$',
        view=Sch_Dist_abs.as_view(),
        name='sch_dist_abs'
    ), 

    url(
        regex=r'^sch_dist_abs/(?P<pk>\d+?)/$',
        view=Sch_Dist_abs.as_view(),
        name='sch_dist_abs'
    ), 

    url(
        regex=r'^sch_edist_abs/$',
        view=Edn_dist_abs.as_view(),
        name='sch_edist_abs'
    ),  

    url(
        regex=r'^sch_block_abs/(?P<pk>\d+?)/$',
        view=Sch_Blk_abs.as_view(),
        name='sch_block_abs'
    ), 

    url(
        regex=r'^sch_block_abs/$',
        view=Sch_Blk_abs.as_view(),
        name='sch_block_abs'
    ),       

    url(
        regex=r'^sch_srep_bi/$',
        view=Sch_sr_bi.as_view(),
        name='sch_srep_bi'
    ),  

    url(
        regex=r'^sch_srep_ai/$',
        view=Sch_sr_ai.as_view(),
        name='sch_srep_ai'
    ),  

    url(
        regex=r'^sch_srep_ii/$',
        view=Sch_sr_ii.as_view(),
        name='sch_srep_ii'
    ), 

    url(
        regex=r'^sch_srep_cs/$',
        view=Sch_sr_cs.as_view(),
        name='sch_srep_cs'
    ), 

    url(
        regex=r'^sch_srep_ti/$',
        view=Sch_sr_ti.as_view(),
        name='sch_srep_ti'
    ), 

    url(
        regex=r'^sch_srep_nti/$',
        view=Sch_sr_nti.as_view(),
        name='sch_srep_nti'
    ), 

    url(
        regex=r'^sch_srep_ld/$',
        view=Sch_sr_ld.as_view(),
        name='sch_srep_ld'
    ), 
    url(
        regex=r'^sch_srep_bd/$',
        view=Sch_sr_bd.as_view(),
        name='sch_srep_bd'
    ), 

    url(
        regex=r'^sch_srep_bad/$',
        view=Sch_sr_bad.as_view(),
        name='sch_srep_bad'
    ), 


    url(
        regex=r'^sch_srep_sd/$',
        view=Sch_sr_sd.as_view(),
        name='sch_srep_sd'
    ), 


    url(
        regex=r'^sch_srep_ict/$',
        view=Sch_sr_ict.as_view(),
        name='sch_srep_ict'
    ),


    url(
        regex=r'^sch_srep_ppd/$',
        view=Sch_sr_ppd.as_view(),
        name='sch_srep_ppd'
    ),


    url(
        regex=r'^sch_dist_repbi/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_bi.as_view(),
        name='sch_dist_repbi'
    ), 
     
    url(
        regex=r'^sch_dist_repai/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_ai.as_view(),
        name='sch_dist_repai'
    ), 
    url(
        regex=r'^sch_dist_repii/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_ii.as_view(),
        name='sch_dist_repii'
    ), 
    url(
        regex=r'^sch_dist_repcs/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_cs.as_view(),
        name='sch_dist_repcs'
    ),     
    url(
        regex=r'^sch_dist_repti/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_ti.as_view(),
        name='sch_dist_repti'
    ),

    url(
        regex=r'^sch_dist_repnti/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_nti.as_view(),
        name='sch_dist_repnti'
    ),
    url(
        regex=r'^sch_dist_repld/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_ld.as_view(),
        name='sch_dist_repld'
    ), 
    url(
        regex=r'^sch_dist_repbd/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_bd.as_view(),
        name='sch_dist_repbd'
    ),     

    url(
        regex=r'^sch_dist_repbad/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_bad.as_view(),
        name='sch_dist_repbad'
    ),
    url(
        regex=r'^sch_dist_repsd/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_sd.as_view(),
        name='sch_dist_repsd'
    ),
    url(
        regex=r'^sch_dist_repict/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_ict.as_view(),
        name='sch_dist_repict'
    ),
    url(
        regex=r'^sch_dist_repppd/(?P<blk>\d+?)/(?P<code>\d+?)/(?P<code1>\d+?)/$',
        view=Sch_blkr_ppd.as_view(),
        name='sch_dist_repppd'
    ),    

    url(
        regex=r'^sch_dist_repbi/(?P<blk>\d+?)/$',
        view=Sch_blkr_bi.as_view(),
        name='sch_dist_repbi'
    ), 

    url(
        regex=r'^sch_dist_repbi/$',
        view=Sch_blkr_bi.as_view(),
        name='sch_dist_repbi'
    ), 

    url(
        regex=r'^sch_dist_repai/(?P<blk>\d+?)/$',
        view=Sch_blkr_ai.as_view(),
        name='sch_dist_repai'
    ), 
    url(
        regex=r'^sch_dist_repai/$',
        view=Sch_blkr_ai.as_view(),
        name='sch_dist_repai'
    ),     
    url(
        regex=r'^sch_dist_repii/(?P<blk>\d+?)/$',
        view=Sch_blkr_ii.as_view(),
        name='sch_dist_repii'
    ),
    url(
        regex=r'^sch_dist_repii/$',
        view=Sch_blkr_ii.as_view(),
        name='sch_dist_repii'
    ),     
    url(
        regex=r'^sch_dist_repcs/(?P<blk>\d+?)/$',
        view=Sch_blkr_cs.as_view(),
        name='sch_dist_repcs'
    ),
    url(
        regex=r'^sch_dist_repcs/$',
        view=Sch_blkr_cs.as_view(),
        name='sch_dist_repcs'
    ),         
    url(
        regex=r'^sch_dist_repti/(?P<blk>\d+?)/$',
        view=Sch_blkr_ti.as_view(),
        name='sch_dist_repti'
    ),
    url(
        regex=r'^sch_dist_repti/$',
        view=Sch_blkr_ti.as_view(),
        name='sch_dist_repti'
    ),
    url(
        regex=r'^sch_dist_repnti/(?P<blk>\d+?)/$',
        view=Sch_blkr_nti.as_view(),
        name='sch_dist_repnti'
    ),
    url(
        regex=r'^sch_dist_repnti/$',
        view=Sch_blkr_nti.as_view(),
        name='sch_dist_repnti'
    ),
    url(
        regex=r'^sch_dist_repld/(?P<blk>\d+?)/$',
        view=Sch_blkr_ld.as_view(),
        name='sch_dist_repld'
    ), 
    url(
        regex=r'^sch_dist_repld/$',
        view=Sch_blkr_ld.as_view(),
        name='sch_dist_repld'
    ),
     
    url(
        regex=r'^sch_dist_repbd/(?P<blk>\d+?)/$',
        view=Sch_blkr_bd.as_view(),
        name='sch_dist_repbd'
    ),

    url(
        regex=r'^sch_dist_repbd/$',
        view=Sch_blkr_bd.as_view(),
        name='sch_dist_repbd'
    ),   

    url(
        regex=r'^sch_dist_repbad/(?P<blk>\d+?)/$',
        view=Sch_blkr_bad.as_view(),
        name='sch_dist_repbad'
    ),
    url(
        regex=r'^sch_dist_repbad/$',
        view=Sch_blkr_bad.as_view(),
        name='sch_dist_repbad'
    ),    
    url(
        regex=r'^sch_dist_repsd/(?P<blk>\d+?)/$',
        view=Sch_blkr_sd.as_view(),
        name='sch_dist_repsd'
    ),
    url(
        regex=r'^sch_dist_repsd/$',
        view=Sch_blkr_sd.as_view(),
        name='sch_dist_repsd'
    ),    
    url(
        regex=r'^sch_dist_repict/(?P<blk>\d+?)/$',
        view=Sch_blkr_ict.as_view(),
        name='sch_dist_repict'
    ),
    url(
        regex=r'^sch_dist_repict/$',
        view=Sch_blkr_ict.as_view(),
        name='sch_dist_repict'
    ),
    url(
        regex=r'^sch_dist_repppd/(?P<blk>\d+?)/$',
        view=Sch_blkr_ppd.as_view(),
        name='sch_dist_repppd'
    ),    
    url(
        regex=r'^sch_dist_repppd/$',
        view=Sch_blkr_ppd.as_view(),
        name='sch_dist_repppd'
    ), 

    url(
        regex=r'^sch_rep/(?P<blk>\d+?)/(?P<code>\d+?)/$',
        view=Sch_srep.as_view(),
        name='sch_rep'
    ),
    url(
        regex=r'^sch_rep1/(?P<blk>\d+?)/(?P<code>\d+?)/$',
        view=Sch_srep1.as_view(),
        name='sch_rep'
    ),    
    url(
        regex=r'^sch_rep/(?P<blk>\d+?)/$',
        view=Sch_srep.as_view(),
        name='sch_rep'
    ),   

    url(
        regex=r'^sch_rep1/(?P<blk>\d+?)/$',
        view=Sch_srep1.as_view(),
        name='sch_rep'
    ), 

    url(
        regex=r'^deo_rep/$',
        view=Deo_srep.as_view(),
        name='deo_rep'
    ),        
    # url(r'^admin/', include(admin.site.urls)),
)