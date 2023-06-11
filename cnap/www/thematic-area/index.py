import frappe

def get_services_by_sector(sector):
    print(sector)
    services = frappe.db.get_list('CNAP Service',
                                    fields=['identifier', 'keyword', 'sector'],
                                    filters={'sector': sector}
                                )
    print(services)
    return services

def get_sectors(thematic_area):
    print(thematic_area)
    sectors = frappe.db.get_list('CNAP Sector',
                                    fields=['name', 'thematic_area'],
                                    filters={'thematic_area': thematic_area}
                                )
    print(sectors)
    return sectors    

def get_context(context):

    area = frappe.form_dict.docname
    sectors = get_sectors(area)
    i = 0
    for sector in sectors:
        services = get_services_by_sector(sector.name)
        sectors[i].services = services
        i = i + 1    
    context.sectors = sectors
    context.area = area
    return context