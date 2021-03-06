from svgsamplescollection import SamplesCollection
mySampCol = SamplesCollection()
mySampCol.add_creator('Giacomo Marchioro')
mySampCol.publisher = 'Università di Verona'
mySampCol.name = 'Test silver'
mySampCol.set_samplesholder_dimension.A4()
mySampCol.set_sample_dimension.Microscope_slide()
mySampCol.set_number_of_samples(15)
mySampCol.margin_top_mm = 15
mySampCol.margin_bottom_mm = 15
mySampCol.minh_spacing_mm = 10
mySampCol.minv_spacing_mm = 5
mySampCol.create_sample_holder()
mySampCol.add_step("Silver samples are cut and fixed to the sample holder.")
mySampCol.populate_with_samples(material='silver')
mySampCol.add_step("Silver samples with ids ranging from 1 to 8 are ceased using a graver.")
for sample in mySampCol.samples[1:8]:
    sample.add_treatment("cheased", "graver")
mySampCol.add_step("A nitrocellulose lacquer is used to protect the silver samples.")
for sample in mySampCol.samples[1:5]:
    sample.add_layer("varnish", "nitorcellulose lacquer", width_percent=0.7)
mySampCol.add_step("All the samples are cleaned using acetone.")
for sample in mySampCol.samples:
    sample.add_treatment("cleaning", "acetone",width_percent=0.5)
mySampCol.insert_alignment_MTF_standard()
mySampCol.insert_scalebar()
mySampCol.insert_standard()
# we save the svg file with all the information
mySampCol.save_svg()
# and the masks
mySampCol.save_masks_svg()
mySampCol.save_masks_dxf()
